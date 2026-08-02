# Opaque System Analysis Evaluations

This compatibility suite qualifies the routing, evidence, safety, and handoff boundaries of `opaque-system-analysis`.

- `happy-path`: recovers only the minimum contract needed for a safe replacement integration.
- `edge-case`: preserves uncertainty when the distinguishing observation is unsafe, unavailable, or unsupported by the local toolchain.
- `failure-case`: rejects misrouting into ordinary diagnosis, credential bypass, unverified reverse-engineering assumptions, and production changes.

Recorded results are repository-maintainer compatibility assessments against the current `SKILL.md` contract.
