# Drive Artifact Contract

## Purpose

This contract defines how `project-second-brain` handles non-textual project artifacts without turning GitHub into a binary document store or creating a second source of truth.

The Project Memory remains GitHub-versioned and Obsidian-compatible. Google Drive is an external artifact store for non-textual project, reference, and delivery files that are not required for repository build, test, runtime, or source control.

## Storage boundary

### Keep in the repository

Keep an artifact in the project repository when at least one of the following is true:

- it is source code or configuration,
- it is required to build, test, package, deploy, or run the project,
- it is a repository-native design/runtime asset such as an icon, fixture, embedded media file, model file, or other binary dependency,
- the repository is already the authoritative producer location for that artifact.

Repository-resident binary assets are referenced from Project Memory like any other canonical repository artifact. They are not copied to Drive merely because they are binary.

### Store in Google Drive

Use the documented project Drive folder for non-textual artifacts that are documentary, referential, review-oriented, distributable, or final-delivery material and are not required by the repository itself. Typical examples include:

- PPT/PPTX, DOC/DOCX, XLS/XLSX,
- PDF,
- PNG/JPEG/TIFF and other review/export images,
- EPUB and other packaged publications,
- audio and video,
- ZIP or other packaged handoff bundles,
- Google Docs, Sheets, and Slides that are the canonical external artifact.

Do not re-upload an artifact that already has an authoritative external location. Register and link the authoritative object instead.

## Project Drive folder

Each Project Memory has at most one canonical Drive project folder for externally stored artifacts.

Preferred resolution order:

1. Reuse the folder already recorded in `state.json`.
2. Reuse an explicitly established project Drive folder from the current handoff or project documentation.
3. Reuse an existing exact project folder only after verifying its identity and suitability.
4. Otherwise create a private project folder below a configured Drive parent. If no parent has been configured, use a `Skillz Projects` container in My Drive and create `<projectId>` below it.

After creation or discovery, persist the Drive folder ID and observed URL. From that point onward, identify the folder by ID rather than by name.

Do not change sharing permissions merely to satisfy this contract. Preserve existing sharing state and keep newly created folders private unless the user explicitly requests other sharing.

## Project Memory representation

`docs/project-memory/ASSETS.md` is the human-readable and Obsidian-compatible manifest. `state.json` carries the compact machine-readable projection.

Minimum `ASSETS.md` header:

```markdown
# External Assets

- Provider: Google Drive
- Project folder URL: `observed-drive-folder-url`
- Folder ID: `observed-folder-id`
- Last verified: `2026-09-10T12:00:00+02:00`
```

Each registered asset records at least:

- stable local asset ID, e.g. `ASSET-001`,
- purpose/role,
- canonical file name,
- Drive file ID,
- observed Drive URL,
- MIME type or artifact type,
- lifecycle state: `working`, `review`, `released`, `superseded`, or `archived`,
- producing skill or source,
- related Project Memory event,
- last verified timestamp,
- revision/checksum/modified time when available and materially useful.

Example:

```markdown
| ID | Role | Artifact | Drive URL | State | Producer | Event | Verified |
|---|---|---|---|---|---|---|---|
| ASSET-004 | final presentation | NDD Review.pptx | `observed-drive-file-url` | released | presentation workflow | EVT-... | 2026-09-10 |
```

Do not invent Drive IDs, URLs, revisions, checksums, or verification timestamps. Record only connector-observed or otherwise verified values.

## `state.json` projection

When a Drive artifact store exists, use the additive `artifactStore` and `externalArtifacts` fields:

```json
{
  "schemaVersion": 2,
  "artifactStore": {
    "provider": "google-drive",
    "folderId": "observed-folder-id",
    "folderUrl": "observed-folder-url",
    "folderName": "project-id",
    "lastVerifiedAt": "2026-09-10T12:00:00+02:00"
  },
  "externalArtifacts": [
    {
      "id": "ASSET-004",
      "role": "final-presentation",
      "name": "NDD Review.pptx",
      "mimeType": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
      "driveFileId": "observed-file-id",
      "url": "observed-drive-file-url",
      "status": "released",
      "producer": "presentation-workflow",
      "event": "docs/project-memory/events/EVT-....md",
      "verifiedAt": "2026-09-10T12:00:00+02:00"
    }
  ]
}
```

Existing Project Memory states without external assets may remain schema version 1. Upgrade to schema version 2 when `artifactStore` or `externalArtifacts` is first materialized; do not rewrite historical event notes solely for the schema upgrade.

## Upload and update behavior

1. Classify the artifact using the storage boundary above.
2. Resolve and verify the canonical project Drive folder.
3. Upload the new file or update the existing canonical Drive file only when that file is intentionally mutable.
4. Read back metadata after a write and capture the observed file ID, URL, MIME type, parent, and modification state.
5. Register or update the asset in `ASSETS.md` and `state.json`.
6. Link the asset from the Project Memory event that produced, reviewed, released, superseded, or consumed it.
7. Include the asset manifest and Drive folder reference in the next `projectMemory` handoff.

For approved/frozen deliverables, prefer a new explicitly versioned file or an otherwise auditable version transition instead of silently replacing a released artifact. A superseded asset remains in the manifest with its prior relation intact.

## Event linkage

A Project Memory event may reference external assets in frontmatter or body. Use stable asset IDs plus observed Drive links, for example:

```yaml
external_outputs:
  - asset_id: ASSET-004
    drive_file_id: observed-file-id
    manifest: ../ASSETS.md
```

The event remains an index/evidence record, not a duplicate of the binary artifact.

## Handoff extension

When the project has external assets, extend the normal handoff as follows:

```json
{
  "projectMemory": {
    "root": "docs/project-memory/INDEX.md",
    "state": "docs/project-memory/state.json",
    "latestEvent": "docs/project-memory/events/EVT-....md",
    "assetIndex": "docs/project-memory/ASSETS.md",
    "artifactStore": {
      "provider": "google-drive",
      "folderId": "observed-folder-id",
      "folderUrl": "observed-folder-url"
    }
  }
}
```

Downstream skills must reuse this folder rather than creating their own parallel project artifact folders.

## Failure rules

Treat the artifact step as incomplete when:

- the Drive write has not been read back or otherwise verified,
- the recorded file/folder ID or URL is guessed rather than observed,
- the artifact was uploaded outside the canonical project folder without an explicit documented reason,
- a Drive copy duplicates another authoritative external source without need,
- a repository runtime/build asset was moved out of the repository solely because it is binary,
- a released/frozen artifact was silently overwritten without an auditable version transition,
- a new parallel Drive project folder was created although a canonical one was already recorded.

A Drive outage or unavailable connector is a pending external state, not a reason to claim that the artifact has been stored. Record the pending item and preserve the next action.