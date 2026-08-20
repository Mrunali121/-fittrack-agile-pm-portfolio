# Project Retrospective — FitTrack MVP

**Format:** Start / Stop / Continue
**Participants:** Full team (PM, 2x Dev, Design, QA)

## What went well
- Pre-agreeing a "must cut" list at charter stage (R-03) meant scope decisions during
  the project were fast and low-drama — no late-stage negotiation with the sponsor.
- Routing all mid-sprint feature requests through the PM (R-04) prevented scope creep
  from silently eating sprint capacity — used successfully in Sprint 2.
- Investing unstoried effort into infra/architecture in Sprint 1 paid off — Sprints 2
  and 3 had smoother, more predictable velocity.
- Weekly async status reports kept the sponsor aligned without needing extra meetings.

## What didn't go well
- Story point estimates for step-tracking work (FT-6) were initially too optimistic —
  the sensor API spike should have happened in Sprint 0, not absorbed into Sprint 1
  capacity planning.
- QA was under-resourced early on — regression suite (FT-12) wasn't started until
  Sprint 3, leaving less buffer than ideal for a release sprint.

## Action items
| Action | Owner | Status |
|---|---|---|
| Add a technical spike step to Sprint 0 checklist for future projects with unfamiliar APIs | PM | Adopted for next project |
| Bring QA into backlog grooming from Sprint 1, not Sprint 3 | PM + QA Lead | Adopted |
| Keep the "pre-agreed cut list" practice for all future project charters | PM | Adopted |
| Formalize the mid-sprint change-request process used in Sprint 2 into a written team norm | PM | Documented in team wiki |

## Outcome
MVP delivered on time, 0 critical bugs, 500 beta users onboarded. Day-7 retention
came in at 34% against a 30% target.
