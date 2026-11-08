---
name: hack-retro
description: Post-hackathon retrospective that makes the system improve. Use after judging/results, or when the user wants to reflect on a hackathon. Captures results, judge feedback, time sinks, and what the winners did better; appends evidence-based rules to the shared lessons file and proposes edits to the hack-* skills themselves.
---

# hack-retro: compound the learning

This is the step that makes each hackathon raise the odds for the next one. Do it within 48 hours, while memory is fresh.

## 1. Gather evidence (ask the user; pull the rest from `.hackathon/`)
- Result (placement, which tracks were won or lost)
- Any direct judge feedback or reactions during the demo (what made them lean in, what questions they asked)
- Who won, and **honestly why**: look at winners' Devpost pages and videos
- Planned vs. actual timing: compare `state.md` and `plan.md` checkpoints to `build-log.md`
- Where `hack-judge`'s predicted score was wrong compared with reality (calibration)

## 2. Analyze
- Separate **decision quality from outcome**. A good idea that lost to variance isn't a bad decision; an unrehearsed demo that happened to win still is one.
- Identify the 1–3 highest-leverage changes. Prefer specific, testable rules ("spike the riskiest API in the first hour") over vague ones ("manage time better").

## 3. Write
1. Append an entry to `~/.claude/hack-hackathon/playbook/lessons.md` in its documented format.
2. If a lesson implies a change to a skill (a new kill rule, a different phase budget, a new checklist item), show the exact diff to the relevant `~/.claude/hack-hackathon/skills/<skill>/SKILL.md` and apply it if the user agrees.
3. Remind the user to commit and push the hack-hackathon repo so the improvement persists:
   `cd ~/.claude/hack-hackathon && git add -A && git commit -m "retro: <event>" && git push`

## 4. Calibrate the judge
If `hack-judge` was systematically too generous or harsh, add a calibration note to `lessons.md` (e.g. "judge sim overrated design by ~2 pts at infra-heavy events").
