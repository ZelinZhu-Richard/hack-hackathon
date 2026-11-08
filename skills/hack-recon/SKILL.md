---
name: hack-recon
description: Research a hackathon before ideating. Use when starting a hackathon or when the user shares a hackathon URL/Devpost page. Extracts judging criteria and weights, judges, sponsors and prize tracks, rules (pre-existing code, team size, submission requirements), and past winners, and writes .hackathon/recon.md with a scoring rubric used by later stages.
---

# hack-recon: know the objective function before you optimize

Output: `.hackathon/recon.md`. Time box: **20 min** for ≥24h events, **10 min** for shorter ones. Stop when the box runs out, even if research feels incomplete, and mark unknowns as unknown.

## Sources (use WebSearch / WebFetch; ask the user to paste content if pages are behind login)
1. Official site + rules page + Devpost page (Overview, Rules, Prizes, Judges tabs)
2. Past editions: "<event> <previous year> winners", the Devpost project gallery filtered to winners
3. Each named judge: role, company, and what they have publicly cared about (1–2 lines each, no deep stalking)
4. Each sponsor prize: what API/product they want used and the exact eligibility wording
5. The event's Discord/Slack announcements if the user can paste them

## Extract into `.hackathon/recon.md`

```markdown
# Recon: <event>

## Judging rubric
| Criterion | Weight | What "5/5" looks like for this event |
|---|---|---|
(If weights are unpublished, assume equal and say so. If no criteria are published, use: Impact, Technical difficulty, Originality, Design/UX, Presentation.)

## Judges
- <name> (<role>): likely values <X>, so show them <Y>

## Prize tracks we could plausibly target
| Track | Prize | Requirement | Competition guess (low/med/high) | Fit notes |

## Rules that constrain us
- Pre-existing code allowed? (critical: if not, no starter templates beyond public libraries/boilerplate)
- Team size, submission format, video length limit, demo format (live / table / stage / video-only)
- Deadline and timezone, and whether late submissions are accepted (assume not)

## Past winners (pattern-match)
| Year | Project | One-line | Why it likely won |
Patterns: <what keeps winning here; what has already been done and should be avoided>

## Unknowns to ask organizers/mentors in person
- ...
```

## Then
- Highlight the **2–3 insights that should change what we build** (e.g. "2 of 4 judges are infra engineers → technical depth is weighted more than the rubric suggests").
- Flag hard constraints that eliminate idea classes (hardware banned, must use sponsor X, etc.).
- Append the key insight to the decisions log in `.hackathon/state.md`. Next stage: `hack-ideate`.
