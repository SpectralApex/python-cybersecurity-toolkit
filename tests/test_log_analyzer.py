import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest


MODULE_PATH = Path(__file__).parents[1] / "log-analyzer" / "log_analyzer.py"
SPEC = importlib.util.spec_from_file_location("log_analyzer", MODULE_PATH)
assert SPEC and SPEC.loader
log_analyzer = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = log_analyzer
SPEC.loader.exec_module(log_analyzer)


class LogAnalyzerTests(unittest.TestCase):
    def test_analyze_lines_counts_events_and_iocs(self):
        lines = [
            "Jan 1 host sshd[1]: Failed password for root from 203.0.113.8 port 22 ssh2\n",
            "Jan 1 host sshd[2]: Failed password for invalid user admin "
            "from 198.51.100.7 port 22 ssh2\n",
            "Jan 1 host sshd[3]: Accepted password for user from 203.0.113.8 port 22 ssh2\n",
            "Jan 1 host sshd[4]: Failed password for root from not-an-ip port 22 ssh2\n",
        ]

        report = log_analyzer.analyze_lines(lines, {"203.0.113.8"})

        self.assertEqual(report["failed_login_count"], 2)
        self.assertEqual(report["unique_source_ips"], 2)
        self.assertEqual(report["source_ip_counts"], {"198.51.100.7": 1, "203.0.113.8": 1})
        self.assertEqual(report["username_counts"], {"admin": 1, "root": 1})
        self.assertEqual(report["matched_iocs"], ["203.0.113.8"])

    def test_load_iocs_ignores_comments_and_invalid_values(self):
        with tempfile.TemporaryDirectory() as directory:
            ioc_file = Path(directory) / "iocs.txt"
            ioc_file.write_text("# test indicators\n203.0.113.8\nnot-an-ip\n198.51.100.7 # note\n")

            self.assertEqual(log_analyzer.load_iocs(ioc_file), {"198.51.100.7", "203.0.113.8"})
