# Portfolio operating contract

## Mission

Advance this repository into a defensive security-engineering portfolio. Preserve useful work and improve it incrementally; do not restart it.

## Required workflow for every change

1. Read `README.md` and `roadmap.md`, inspect the current code and recent changes.
2. Select the highest-value unfinished roadmap item that builds on existing work.
3. Keep all work defensive, legal, authorized, and reproducible. Use only local fixtures, lab data, or explicitly authorized targets.
4. Add or update focused tests and user documentation with each behavior change.
5. Run the relevant tests, formatter, linter, and security checks; fix failures before proposing a change.
6. Review the diff for secrets, credentials, private keys, tokens, and personal data before committing.

## Engineering standards

- Prefer standard-library Python and explicit, typed data structures.
- Design tools for local logs and lab inputs by default; avoid hidden network activity.
- Keep command-line interfaces scriptable and emit JSON where it helps integration.
- Document assumptions, limitations, and safe usage.
- Build integration paths between log analysis, IOC matching, file integrity monitoring, alerting, and dashboards instead of adding isolated demos.

## Safety boundary

Never add malware, credential theft, persistence, evasion, destructive actions, or unauthorized scanning/exploitation. Defensive detection, secure coding, lab exercises, and incident-response automation are in scope.
