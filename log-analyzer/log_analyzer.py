"""Defensive authentication-log analysis with local IOC matching.

The module reads a local log file only. It makes no network requests and is
intended for authorized incident-response and lab workflows.
"""

from __future__ import annotations

import argparse
import ipaddress
import json
import re
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


FAILED_LOGIN_PATTERN = re.compile(
    r"Failed password for (?:invalid user )?(?P<user>\S+) from (?P<ip>\S+)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class FailedLoginEvent:
    """A normalized failed-login event found in a log line."""

    line_number: int
    username: str
    source_ip: str
    raw_line: str


def _is_ip_address(value: str) -> bool:
    try:
        ipaddress.ip_address(value)
    except ValueError:
        return False
    return True


def parse_failed_login(line: str, line_number: int) -> FailedLoginEvent | None:
    """Return a normalized event when *line* contains an SSH failure."""

    match = FAILED_LOGIN_PATTERN.search(line)
    if match is None:
        return None

    source_ip = match.group("ip")
    if not _is_ip_address(source_ip):
        return None

    return FailedLoginEvent(
        line_number=line_number,
        username=match.group("user"),
        source_ip=source_ip,
        raw_line=line.rstrip("\n"),
    )


def load_iocs(path: Path | None) -> set[str]:
    """Load one IP address per line, ignoring blank lines and comments."""

    if path is None:
        return set()

    indicators: set[str] = set()
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        candidate = raw_line.split("#", maxsplit=1)[0].strip()
        if candidate and _is_ip_address(candidate):
            indicators.add(candidate)
    return indicators


def analyze_lines(lines: Iterable[str], iocs: set[str] | None = None) -> dict[str, object]:
    """Analyze SSH auth-log lines and return serializable defensive findings."""

    indicators = iocs or set()
    events = [
        event
        for line_number, line in enumerate(lines, start=1)
        if (event := parse_failed_login(line, line_number)) is not None
    ]
    source_counts = Counter(event.source_ip for event in events)
    user_counts = Counter(event.username for event in events)
    matched_iocs = sorted({event.source_ip for event in events} & indicators)

    return {
        "failed_login_count": len(events),
        "unique_source_ips": len(source_counts),
        "source_ip_counts": dict(sorted(source_counts.items())),
        "username_counts": dict(sorted(user_counts.items())),
        "matched_iocs": matched_iocs,
        "events": [asdict(event) for event in events],
    }


def analyze_log(log_path: Path, ioc_path: Path | None = None) -> dict[str, object]:
    """Read a local log and optionally match it against a local IOC file."""

    with log_path.open("r", encoding="utf-8", errors="replace") as log_file:
        return analyze_lines(log_file, load_iocs(ioc_path))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Analyze SSH failed-login events in a local log file."
    )
    parser.add_argument(
        "log_file", type=Path, help="Path to an authorized local authentication log"
    )
    parser.add_argument("--ioc-file", type=Path, help="Optional file with one IP IOC per line")
    parser.add_argument("--json", action="store_true", help="Print a JSON report")
    args = parser.parse_args()

    report = analyze_log(args.log_file, args.ioc_file)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Failed logins: {report['failed_login_count']}")
        print(f"Unique source IPs: {report['unique_source_ips']}")
        print(f"IOC matches: {', '.join(report['matched_iocs']) or 'none'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
