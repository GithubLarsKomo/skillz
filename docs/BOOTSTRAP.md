# skillz bootstrap

The beta bootstrap path starts from a fresh checkout and installs only portable files recorded in `.skill-sync.json`.

## Prerequisites

- Git
- Python 3.12 or newer
- a fresh checkout of this repository
- an explicit destination directory for installed skills

## One-command validated installation

From the repository root:

```bash
python scripts/bootstrap_skillz.py --target-dir /path/to/installed-skills --skill repository-skill-bootstrap
```

By default the command first runs repository metadata, schema, skill, and evaluation validation. It then verifies every portable source file against the synchronization manifest before copying the selected skill. Repeat `--skill` to install several skills; omit it to install all portable skills.

The destination is intentionally explicit. The beta does not assume a particular agent product, hidden home-directory layout, or installation ID.

## Fast reinstall when repository CI is already trusted

```bash
python scripts/bootstrap_skillz.py --target-dir /path/to/installed-skills --skill repository-skill-bootstrap --skip-repo-validation
```

This skips repository-wide checks but still verifies all source and installed portable-file hashes. It is intended for repeated local installs, not for establishing trust in a new checkout.

## Expected result

The command prints one JSON object with `status: ready`, the absolute target directory, and the installed skill names/paths. A non-zero exit means no successful installation should be assumed.

## Recovery

The installer never deletes unrelated files, modifies the source checkout, commits, pushes, calls a provider, or accesses credentials. If an installation must be reset, remove the explicitly chosen destination directory and run the command again.
