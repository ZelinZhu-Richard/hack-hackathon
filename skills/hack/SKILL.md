---
name: hack
description: Hackathon command center. Use at the start of a hackathon, whenever the user asks "what should I do now" during one, or to check time/phase status. Sets up the .hackathon/ state folder, tracks the clock, and routes to the right pipeline stage (recon, ideate, judge, scope, build, pitch, submit, retro).
---

# /hack — hackathon orchestrator

You run a time-boxed pipeline whose single objective is **maximizing the judges' score**, not building the best software. Every stage reads and writes files in `.hackathon/` at the root of the current project so stages hand off cleanly and survive context resets.

Shared knowledge lives in `~/.claude/hack-hackathon/playbook/`:
- `principles.md` — what wins (read once per session, before routing)
- `lessons.md` — the user's own lessons from past hackathons (read it; these override generic principles when they conflict)

## 1. Initialize (only if `.hackathon/state.md` does not exist)

Ask for whatever is missing, in one message, nothing more:
- Hackathon name + URL (rules / judging page)
- Start and end time **with timezone**, and the submission deadline if different
- Team: names + strengths (frontend, backend, ML, design, pitching)
- Any theme, required tech, or prize tracks already known

Then create `.hackathon/state.md`:

```markdown
# <Hackathon name>
- URL:
- Start: <ISO time + tz>   End: <ISO time + tz>   Submission deadline: <ISO>
- Duration: <h>
- Team: <name — strengths>, ...
- Current phase: recon
- Feature freeze at: <computed, see table>
- Submit-draft at: <deadline − 2h, or − 30 min for events < 12h>

## Decisions log
<!-- append: time — decision — why -->
```

## 2. Phase budget

Compute absolute clock times from the duration and write them into `state.md`.

| Phase | Share of total time | Exit criterion |
|---|---|---|
| recon + ideate + judge | 0–10% | one idea chosen, logged in decisions |
| scope | 10–13% | `.hackathon/plan.md` with demo script and cut list |
| build: walking skeleton | 13–35% | demo path runs end-to-end, even if ugly/hardcoded |
| build: depth + polish | 35–75% | the "wow moment" works reliably |
| **feature freeze** | 75% | no new features after this, only bug fixes + demo |
| pitch + backup video | 75–90% | rehearsed ≥3× under time limit |
| submit | 90–100% | submitted with ≥30 min slack |

For events < 12h, compress recon+ideate to ≤45 min total. Do not let ideation run over. A mediocre idea executed well beats a great idea that is half-built.

## 3. Route

Every time this skill runs:
1. Read `state.md`, check current time (`date`), compute time remaining and the % elapsed.
2. Compare against the phase budget. If behind, **say so bluntly** and name what to cut.
3. Recommend the next skill and why:

| If... | Run |
|---|---|
| no `recon.md` | `hack-recon` |
| no `idea.md` | `hack-ideate` (it calls `hack-judge` to pick) |
| no `plan.md` | `hack-scope` |
| building | `hack-build` (checkpoint mode) |
| past feature freeze | `hack-pitch` |
| within 3h of deadline, or a draft not submitted | `hack-submit` |
| event over | `hack-retro` |

4. Update `Current phase` in `state.md`.

## Rules for you during the event
- Default to action. Don't run long deliberations; the clock is the scarcest resource.
- Every non-trivial decision → one line in the decisions log.
- If the user is about to start a new feature after freeze, push back once, clearly.
- Remind about sleep / food at roughly 30% and 60% marks on 24h+ events. Tired teams demo badly.
