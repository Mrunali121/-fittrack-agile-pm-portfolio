# Risk Register — FitTrack MVP

| ID | Risk | Likelihood | Impact | Score (L×I) | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|---|
| R-01 | OAuth integration takes longer than estimated, delaying Sprint 1 | Medium (3) | Medium (3) | 9 | Timebox to 3 days; fallback to simpler email-link auth if not resolved | Eng Lead | Closed — fallback not needed, OAuth delivered on time |
| R-02 | Step-tracking sensor API behaves inconsistently across iOS versions | Medium (3) | High (4) | 12 | Early spike in Sprint 1 planning to test on 3 iOS versions before committing story points | Dev A | Closed — spike completed, no blockers found |
| R-03 | Team capacity insufficient to hit 6-week MVP deadline with full feature set | High (4) | High (4) | 16 | Pre-agreed "must cut" list with Sponsor at charter stage (social sharing, wearables) so scope can flex without a late renegotiation | PM | Mitigated — social sharing cut per plan, no deadline slip |
| R-04 | Mid-project stakeholder feature requests cause scope creep | High (4) | Medium (3) | 12 | All new requests routed through PM for impact assessment before entering a sprint; sponsor decides add vs. defer | PM | Active — used successfully in Sprint 2 (streak-freeze request deferred) |
| R-05 | Beta user onboarding capacity (Community Manager) not ready in time for launch | Low (2) | High (4) | 8 | Weekly check-in with Community Manager from Sprint 2 onward; invite email drafted by Week 4 | PM | Closed — invites ready ahead of schedule |
| R-06 | Push notification service (3rd-party) has rate limits that affect streak reminders at scale | Low (2) | Medium (3) | 6 | Load-test with 500 simulated users in Sprint 3 QA pass | QA Lead | Closed — passed load test |

## Scoring key
- Likelihood / Impact: 1 (Low) – 4 (High)
- Score ≥ 12: reviewed at every sprint planning session
- Score 6–11: reviewed at sprint review
- Score < 6: monitored, no active review required

## Review cadence
Risk register reviewed at the start of every sprint planning session; new risks can be
raised by any team member and are triaged by the PM within 24 hours.
