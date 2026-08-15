# FitTrack — Agile Project Management Portfolio

**Role:** Scrum Product/Project Manager (simulated project)
**Methodology:** Scrum (2-week sprints)
**Tools referenced:** Jira-style backlog, Confluence-style docs, Google Sheets for tracking

## About this repository

This repository is a portfolio piece demonstrating end-to-end Agile project management
skills, built around a realistic case: **FitTrack**, a mobile fitness-tracking app for a
5-person cross-functional team (1 PM, 2 developers, 1 designer, 1 QA).

Rather than just describing what a PM does, this repo contains the actual working
artifacts a PM produces during a project lifecycle — from chartering through sprint
execution to retrospective.

## Project summary

| | |
|---|---|
| **Product** | FitTrack — mobile app for workout logging, step tracking, and habit streaks |
| **Team size** | 5 (PM, 2x Dev, 1x Designer, 1x QA) |
| **Duration** | 3 sprints (6 weeks), MVP release |
| **Methodology** | Scrum, 2-week sprints |
| **Business goal** | Ship an MVP to 500 beta users within 6 weeks |

## Contents

| File | What it shows |
|---|---|
| [`01-project-charter.md`](01-project-charter.md) | Scope, objectives, stakeholders, success criteria, constraints |
| [`02-product-backlog.csv`](02-product-backlog.csv) | Prioritized backlog with story points, epics, MoSCoW priority |
| [`03-sprint-planning/`](03-sprint-planning) | Sprint goals, committed stories, and capacity planning for each sprint |
| [`04-raci-matrix.md`](04-raci-matrix.md) | Responsibility matrix across all major deliverables |
| [`05-risk-register.md`](05-risk-register.md) | Identified risks, likelihood/impact scoring, mitigation owners |
| [`06-sprint-burndown-chart.png`](06-sprint-burndown-chart.png) | Burndown tracking for Sprint 2, showing a scope-creep recovery |
| [`07-retrospective.md`](07-retrospective.md) | End-of-project retro: what went well, what didn't, action items |
| [`08-status-report-template.md`](08-status-report-template.md) | Weekly stakeholder status report format, filled with a real example |

## Why this structure

Each document mirrors what I'd actually produce on the job:
- **Charter** — alignment tool used once at kickoff to lock scope and success metrics.
- **Backlog** — living document, reprioritized every sprint based on stakeholder feedback.
- **Sprint plans** — capacity-based commitment, not just a wishlist of tickets.
- **RACI** — prevents the classic "I thought you were doing that" failure mode.
- **Risk register** — reviewed at every sprint planning session, not written once and forgotten.
- **Burndown** — used to catch scope creep early (see Sprint 2 — a mid-sprint stakeholder
  request added 8 points, and the chart shows the recovery plan I put in place).
- **Retrospective** — concrete, owned action items, not vague "communicate better" notes.
- **Status report** — the actual weekly format used to keep stakeholders aligned without a meeting.

## Key PM decisions demonstrated

- Cutting a nice-to-have feature (social sharing) from MVP scope after a mid-project
  capacity risk was flagged, to protect the launch date — see `05-risk-register.md` (R-03)
  and `07-retrospective.md`.
- Managing a scope-creep incident in Sprint 2 without blowing the sprint goal — see the
  burndown chart annotation.
- Running structured sprint planning with capacity-based commitment instead of
  over-committing the team — see `03-sprint-planning/`.

---
*This is a self-directed portfolio project built to demonstrate Agile PM methodology and
documentation standards. Team members, company, and app are illustrative.*
