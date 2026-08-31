# Security engineering roadmap

## Current foundation

The repository contains early Python utilities for log analysis, DNS/reconnaissance, packet observation, network monitoring, and web checks. The portfolio direction is defensive security automation: dependable local analysis first, then integrated detection engineering.

## Milestones

1. **Detection foundation — in progress**
   - [x] Structured SSH failed-login analysis with local IOC matching and JSON output.
   - [ ] Add fixture-based parsing for common Linux auth-log variations and a configurable alert threshold.
   - [ ] Add a file-integrity monitor using SHA-256 baselines and explicit authorized paths.

2. **Security telemetry pipeline**
   - Normalize log, integrity, and network events into a shared schema.
   - Add rule-based detection, severity scoring, and Markdown/JSON reports.
   - Add a local dashboard that visualizes findings without exposing data externally.

3. **Operational hardening**
   - Add Docker development environment, CI checks, dependency review, and secret scanning.
   - Add configuration validation, logging, error handling, and test coverage reporting.

4. **Security engineering integration**
   - Add threat-intelligence feed ingestion from user-supplied data with caching and provenance.
   - Demonstrate vulnerability-management and secure-application-development workflows using intentionally vulnerable labs only.
   - Document incident-response runbooks, architecture decisions, and portfolio case studies.

## Selection rule for future runs

Advance the next unfinished item that most improves correctness, testability, or integration of existing components. Do not create a new standalone project while a stronger existing component remains incomplete.
