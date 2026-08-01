# Capability index query CLI

`scripts/query_capabilities.py` is a read-only consumer of `docs/skill-capability-index.json`. It exists to inspect the repository's declared capabilities without reparsing skill source files.

This boundary is intentionally deterministic. It does not perform natural-language matching, semantic similarity, ranking, routing, orchestration, or skill execution.

## Examples

```bash
python scripts/query_capabilities.py --skill disciplined-diagnosis
python scripts/query_capabilities.py --dependencies implement-from-issue
python scripts/query_capabilities.py --dependents disciplined-diagnosis
python scripts/query_capabilities.py --requires agent-handoff
python scripts/query_capabilities.py --output residual-risk-handoff.json
python scripts/query_capabilities.py --evaluation-mode compatibility
python scripts/query_capabilities.py --with-portable-files
python scripts/query_capabilities.py --without-portable-files --json
```

`--json` emits stable machine-readable output. Unknown skills and outputs, unreadable indexes, and unsupported schema versions fail explicitly with a non-zero status.

Output producer lookup is exact. If several skills declare the same output, all declared producers are returned in deterministic order; the CLI does not guess which producer should be chosen.
