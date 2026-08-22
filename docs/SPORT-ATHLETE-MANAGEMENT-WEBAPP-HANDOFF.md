# Sport Athlete Management – WebApp Repository Handoff

Status: architecture handoff; implementation belongs in a separate product repository.

## Decision

The athlete-facing WebApp, API and persistent relational database do **not** live in `GithubLarsKomo/skillz`.

`skillz` owns:

- sport-domain reasoning skills,
- versioned JSON contracts,
- deterministic validation/calculation helpers,
- evaluation fixtures,
- report integrations.

A new dedicated repository will own:

- athlete WebApp/PWA,
- authentication and authorization,
- API service,
- database migrations and persistence,
- operational deployment to Hetzner/Coolify,
- backups, audit storage and retention,
- device/import adapters when added.

This keeps the portable skill system independent from one product implementation.

## Reference pattern: `GithubLarsKomo/grilling`

Reuse the successful architectural qualities of the Grilling app rather than copying it literally:

- dedicated product repository instead of embedding UI into the skill repository,
- small Node.js application with `type: module`,
- static/responsive frontend under `site/`,
- server-side runtime boundary under `src/` / `server.mjs`,
- Docker/Coolify deployment path,
- tests kept beside the product code,
- JSON-driven UI/workflow definitions where they improve determinism,
- explicit runtime status and safe failure behavior.

The athlete app requires stronger security than Grilling because it stores health-adjacent longitudinal data. The Grilling token-as-simple-access-hurdle pattern is therefore **not** sufficient for production athlete data.

## Proposed repository layout

```text
sport-athlete-management-app/
  .github/workflows/
  Dockerfile
  README.md
  package.json
  runtime-config.json
  server.mjs
  site/
    index.html
    assets/
    app/
      api.js
      checkin.js
      training.js
      history.js
      components/
  src/
    app.mjs
    auth/
    api/
    domain/
    persistence/
    adapters/
  migrations/
  contracts/
  tests/
```

Do not duplicate domain contracts manually. Pin/copy a released `sport-athlete-management-v1.schema.json` from `skillz` with provenance or consume it through an automated release process.

## MVP vertical slice

The first product increment should support exactly:

1. athlete login,
2. athlete profile read/update,
3. one active goal/competition context,
4. active mesocycle and microcycle,
5. today's planned session,
6. 20–40 second Morning Check,
7. completed session + duration + session RPE,
8. explainable adaptation decision,
9. versioned next-session revision,
10. audit history.

No wearables, music, advanced analytics or broad psychology module in the first app increment.

## Database ownership

The database is the operational source of truth for the product. Minimum tables:

- `athletes`
- `athlete_profiles`
- `goals`
- `competitions`
- `seasons`
- `macrocycles`
- `mesocycles`
- `microcycles`
- `planned_sessions`
- `planned_session_items`
- `daily_checkins`
- `completed_sessions`
- `completed_session_items`
- `objective_metrics`
- `adaptation_decisions`
- `training_plan_revisions`
- `audit_events`

Use immutable/versioned plan revisions rather than overwriting the reason why a prescription changed.

## API boundary

The app/API translates persistence models to the canonical Skillz contracts. Initial endpoints should cover:

- `/api/v1/athlete/profile`
- `/api/v1/goals`
- `/api/v1/competitions`
- `/api/v1/training/today`
- `/api/v1/training/week`
- `/api/v1/checkins`
- `/api/v1/sessions/{id}/complete`
- `/api/v1/adaptation/evaluate`
- `/api/v1/adaptation/latest`
- `/api/v1/adaptation/history`
- `/api/v1/adaptation/{id}/override`

## Security delta versus Grilling

Required before real athlete use:

- proper authenticated sessions; no repository-stored access tokens,
- passwordless/OIDC or another established identity provider,
- per-athlete authorization checks on every data endpoint,
- CSRF protection where cookie sessions are used,
- secure cookies and TLS-only operation,
- rate limiting and request size limits,
- encrypted backups,
- no secrets in repository/runtime-config,
- audit log for writes and overrides,
- retention/deletion functions,
- GDPR/privacy review before third-party use.

## Deployment target

Primary target is the existing Hetzner/Coolify environment. Preserve a simple container contract comparable to Grilling: one deployable service image, health endpoint, environment-based configuration and no dependency on local developer state.

A separate managed database container/service may be used, but application startup must fail safely if schema version or database connectivity is invalid.

## Acceptance criterion

The product repository is ready for its first real vertical slice when one authenticated athlete can complete profile → planned session → Morning Check → completed session+sRPE → adaptation decision → revised next session, and every state change can be reconstructed from the audit history.
