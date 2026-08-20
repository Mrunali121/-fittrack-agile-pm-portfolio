# Sprint 1 Planning

**Duration:** Weeks 1–2
**Sprint Goal:** Users can sign up and manually log a workout end-to-end.

## Team Capacity
5 people × 2 weeks, minus 1 dev on-call day and 1 team offsite half-day →
**Effective capacity: 34 story points** (based on team's historical velocity of ~35/sprint)

## Committed Stories
| ID | Story | Points | Owner |
|---|---|---|---|
| FT-1 | Email sign-up | 3 | Dev A |
| FT-2 | Onboarding tutorial | 2 | Design + Dev B |
| FT-3 | Log workout type/duration | 5 | Dev A |
| FT-5 | Edit/delete workout entry | 3 | Dev B |

**Committed points: 13** (intentionally conservative — first sprint, new team cadence,
plus foundational architecture work not story-pointed: auth backend, DB schema, CI/CD
pipeline setup, ~18 points of unstoried infra work)

## Definition of Done
- Code reviewed by 1 peer
- Unit tests passing
- QA sign-off on staging
- No P1/P2 bugs open

## Risks flagged at planning
- Auth backend is a new pattern for the team — timeboxed to 3 days, fallback to
  simpler email-link auth if OAuth proves too slow (see Risk Register R-01).

## Outcome
Sprint completed on schedule. All 4 committed stories delivered + infra foundation
laid for Sprint 2. Velocity: 13 points (story-pointed) + infra work.
