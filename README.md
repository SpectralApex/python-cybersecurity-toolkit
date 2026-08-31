# Python Cybersecurity Toolkit

A developing **defensive security-engineering** portfolio built with Python. The project improves existing utilities incrementally and turns them into tested, documented components for authorized labs and local analysis.

## Current capability: authentication-log analysis

`log-analyzer/log_analyzer.py` analyzes local SSH authentication logs. It:

- identifies failed SSH login events;
- normalizes usernames and valid source IP addresses;
- summarizes source and username counts;
- matches source IPs against a user-supplied, local IOC file; and
- produces human-readable or JSON output suitable for downstream automation.

Example, using only authorized local or lab data:

```bash
python log-analyzer/log_analyzer.py /var/log/auth.log --ioc-file iocs.txt --json
```

The IOC file accepts one IP address per line. Empty lines, comments, and invalid values are ignored deliberately.

## Development

```bash
python -m unittest discover -s tests -v
ruff check .
ruff format --check .
```

## Portfolio direction

The roadmap progresses from reliable Python detection utilities to integrated log analysis, file integrity monitoring, IOC matching, threat intelligence, incident response, Docker, CI/CD security, dashboards, and secure application development. See [roadmap.md](roadmap.md) for the active progression and [AGENTS.md](AGENTS.md) for the permanent operating contract.

## Safety and scope

This repository is for defensive security automation, education, and explicitly authorized labs. It must not be used for unauthorized access, destructive actions, credential theft, persistence, malware, or evasion.

## Existing experiments

Existing DNS, packet, network-monitoring, and scanner experiments remain in place. Future work will harden and integrate the defensive components rather than discard useful work for cosmetic reasons.
