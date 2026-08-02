# skillz beta runbook

Version: `0.1.0-beta.1`

## Beta definition

The first beta is successful when a technically proficient user can start from a fresh checkout, validate the repository, install at least one portable skill into an explicit destination, and execute a documented installed-skill path in a new repository without hidden local state or unsafe credential handling.

## Prerequisites

- Git
- Python 3.12 or newer
- a fresh checkout of this repository
- write access to an explicit local destination for installed skills

No provider credential is required for the core beta path. Live provider validation is optional and isolated from normal CI.

## Validate and install

From the repository root:

```bash
python scripts/bootstrap_skillz.py \
  --target-dir /path/to/installed-skills \
  --skill repository-skill-bootstrap
```

The command verifies the portable synchronization manifest and, by default, repository metadata, schema contracts, skills, and evaluation suites before installing. Success prints a JSON result with `status: ready`.

## Primary beta user path

Create a new Git repository and use the installed copy of `repository-skill-bootstrap`:

```bash
mkdir beta-project
cd beta-project
git init
python /path/to/installed-skills/repository-skill-bootstrap/scripts/bootstrap_repository_context.py \
  --repo . \
  --project-name "Beta Project"
```

Expected result:

```text
docs/agents/CONFIG.md
docs/agents/CONTEXT.md
docs/agents/DECISIONS.md
```

The helper refuses to overwrite those files on a second run. Normal CI reproduces this complete path in an isolated temporary project.

## Install more skills

Repeat `--skill` to install several selected skills. Omit `--skill` to install all portable skills currently recorded in `.skill-sync.json`.

The beta deliberately requires an explicit destination. It does not assume a ChatGPT, IDE, home-directory, or agent-product installation layout.

## Update

1. Fetch or pull a reviewed repository update.
2. Run normal repository validation or rerun `bootstrap_skillz.py` without `--skip-repo-validation`.
3. Reinstall the required skills into the explicit destination.
4. Treat any manifest-hash mismatch as a failed update; do not assume the installation succeeded.

Portable skill identity is the YAML frontmatter `name`, not a local installation identifier.

## Verification

Repository-level checks are enforced in GitHub Actions. The beta-specific gates include:

- bootstrap installer unit tests,
- clean-room install-and-use test,
- generated metadata and schema validation,
- dependency/capability graph and resolver tests,
- skill evaluation suites,
- provider qualification/registry tests where applicable.

For a local high-confidence check, use the normal bootstrap command, which runs the repository validation chain before copying skills.

## Reproducible beta bundle

Build the repository beta bundle with:

```bash
python scripts/build_release_bundle.py --output skillz-0.1.0-beta.1.tar
```

The archive uses canonical paths, deterministic metadata and a content-hash manifest. Building twice from the same checkout must produce identical bytes.

The intended Git tag for this state is:

```text
v0.1.0-beta.1
```

The `VERSION` file is the canonical repository version. A tag must match `v` + the exact `VERSION` value.

## Known beta limits

- No package-manager or hosted registry installation is provided.
- Product-specific agent installation metadata is intentionally outside the portable repository contract.
- Provider-backed interpretation is opt-in and remains gated by qualification evidence and explicit human review.
- Query-bearing provider endpoint URLs are intentionally unsupported by the current secrets-free provider config contract.
- The beta proves one installed deterministic skill path; not every skill has an executable helper because many skills are procedural specifications by design.

## Recovery and rollback

Bootstrap installation never deletes unrelated destination data. To reset an installation, remove the explicit destination directory and reinstall from a reviewed checkout.

For a failed repository update, return to the previously reviewed commit or beta tag, rerun the bootstrap command, and reinstall into a clean destination.

Provider qualification promotion is separately transactional: failed post-write registry verification restores the pre-apply files.

## Feedback evidence to capture

For beta use, record:

- repository commit or tag,
- Python version and operating system,
- selected skill names,
- bootstrap exit status,
- whether the primary clean-room path succeeded,
- any undocumented environment assumption,
- any confusing installation or recovery step.

These observations should drive post-beta complementary function slices without weakening the deterministic validation and safety gates established for beta.
