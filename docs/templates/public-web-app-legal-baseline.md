# Public Web App Legal Baseline Template

Use this template for publicly deployed browser apps, PWAs and websites. It is an engineering/release-completeness aid, not legal advice.

## Reference implementation pattern

A proven reference is `GithubLarsKomo/exam-trainer-framework` with:

- `public/impressum.html`
- `public/datenschutz.html`
- `public/legal.css`
- `docs/public-deployment-legal.md`
- `e2e/legal.spec.ts`

Copy the structure, never unverified factual claims.

## 1. Operator identity

- Operator / responsible person: `[OPERATOR_NAME]`
- Serviceable postal address: `[STREET]`, `[POSTCODE] [CITY]`, `[COUNTRY]`
- Monitored email: `[EMAIL]`
- Legal form: `[PRIVATE_INDIVIDUAL | COMPANY_FORM | NOT_APPLICABLE]`
- Register / registration number: `[VALUE | NOT_APPLICABLE]`
- Additional media-law responsibility block required: `[YES/NO + BASIS]`

No unresolved placeholder may ship publicly.

## 2. Mandatory public surfaces

Create and verify:

- `public/impressum.html` or equivalent route,
- `public/datenschutz.html` or equivalent route,
- shared accessible legal styling,
- links from the public app shell in one interaction,
- direct URL access without requiring app state,
- mobile readability at the minimum supported viewport,
- return path back to the application.

## 3. Hosting and infrastructure facts

Record evidence, not assumptions:

- hosting provider and legal entity,
- hosting product / region where relevant,
- reverse proxy / ingress,
- access-log state,
- application/container log driver,
- rotation / retention criterion,
- backup location and retention,
- DNS/CDN/proxy provider,
- uptime monitoring,
- error reporting,
- WAF/security logging,
- other infrastructure recipients.

Do not copy quantitative log-retention statements from another deployment unless the effective configuration has been verified for this deployment.

## 4. Application data flows

Document whether the application uses:

- localStorage / IndexedDB / Cache API / service worker,
- accounts and authentication,
- backend synchronization,
- cloud saves,
- analytics,
- telemetry,
- advertising/tracking,
- error reporting,
- external fonts/scripts,
- maps/tiles,
- embedded video/audio/social content,
- payment providers,
- AI/LLM APIs,
- push notifications,
- multiplayer / realtime services,
- import/export and backups.

For each non-local flow record purpose, data categories, recipient/provider, legal basis where applicable, retention criterion and whether consent is required.

## 5. Privacy-notice wording rules

The privacy notice should at minimum cover:

1. responsible person/operator,
2. local-first/local-storage behavior,
3. hosting and server requests,
4. cookies/tracking/similar technologies,
5. recipients/transfers,
6. storage duration or evidence-backed criteria,
7. data-subject rights,
8. automated decisions if applicable,
9. change trigger for future data-flow changes.

Never claim a fixed retention period when the infrastructure only has size/count-based rotation or when retention has not been verified.

## 6. Automated acceptance

Recommended E2E assertions:

- app shell exposes `Impressum` and `Datenschutz`,
- both URLs return successfully,
- operator name/address/email are present,
- no operator placeholders remain,
- legal pages work at mobile viewport,
- privacy text contains the actual local/remote data-flow model,
- privacy text does not assert stale or unverified logging/retention behavior.

## 7. Change triggers

Re-run the legal baseline before release whenever adding or changing:

- hosting/infrastructure,
- accounts/authentication,
- cloud synchronization,
- analytics/telemetry,
- tracking/cookies,
- external embeds,
- monitoring/error reporting,
- maps/CDNs/external assets,
- multiplayer/realtime,
- AI APIs,
- payments,
- backups or retention.

## 8. Release decision record

```markdown
# Public deployment legal baseline

## Operator
...

## Legal surfaces
- Impressum: PASS|BLOCKED
- Datenschutz: PASS|BLOCKED
- one-interaction app links: PASS|BLOCKED
- direct URL: PASS|BLOCKED
- mobile acceptance: PASS|BLOCKED

## Infrastructure evidence
...

## Application data flows
...

## Open blockers
...

## Qualified legal review
required|recommended|not currently requested
```
