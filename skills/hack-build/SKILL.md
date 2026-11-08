---
name: hack-build
description: Execution rules and checkpoint reviews while building a hackathon project. Use during the build phase, when the user asks for a checkpoint/status check, when they're stuck or behind schedule, or when they want to add a feature. Enforces walking-skeleton-first, demo-path priority, safe commits, and feature freeze against .hackathon/plan.md.
---

# hack-build: ship the demo path, protect it, then deepen

Inputs: `plan.md`, `state.md`. Keep a running log in `.hackathon/build-log.md`.

## Build rules (apply to all code you write in this phase)
1. **Demo path first.** Before writing anything, check whether it's on the demo script in `plan.md`. If not, ask whether it's worth it now.
2. **Walking skeleton before depth.** Get the whole flow running end-to-end with stubs, then replace stubs with real logic in order of what the judge sees.
3. **Deploy early.** Get a public URL (Vercel / Render / Fly / ngrok / HF Spaces) by the walking-skeleton checkpoint. Deploying for the first time at hour 20 is how demos die.
4. **Commit every working state** with clear messages. When the demo path works, `git tag demo-safe-N`. You can always roll back to something demoable.
5. **Seed data is a feature.** Craft realistic, emotionally resonant demo data (a believable person, a believable problem). Lorem ipsum loses points.
6. **Demo-proof external calls.** For LLM/API calls on the demo path: timeouts, a retry, and a cached-response fallback toggled by an env var (`DEMO_MODE=1`). Venue Wi-Fi fails.
7. **Visible depth.** Build one thing that *shows* the hard part: a live log panel, a trace view, a "what the model sees" toggle, a metrics readout.
8. **No yak-shaving.** If a bug costs > 30 min, stop and choose: hardcode it, cut it, or ask a mentor.
9. If the event bans pre-existing code (check `recon.md`), write the code fresh here. Don't paste from old projects.

## Parallelism
With teammates: split by vertical slice or by clear interface (agree on the API/JSON shape first, mock it on both sides). With Claude subagents/worktrees: hand off isolated, well-specified pieces (a scraper, a UI component, a data-cleaning script), never the core wow logic you'll need to explain to judges.

## Checkpoint mode (run when the user asks for status, or at each checkpoint time in plan.md)
1. `date` → % elapsed vs. `state.md` budget.
2. Which plan checkpoint should be done by now? Is it actually done (run it, don't take it on faith)?
3. Verdict: **on track / behind / critically behind**.
4. If behind: name the cut-list items to drop *now* and the pivot rule if one applies. Be direct.
5. Every other checkpoint, run a quick `hack-judge` on the current state (demo script + what works) to catch drift from what scores.
6. Append to `build-log.md`: time, status, what's done, what was cut, next 2 hours.

## Feature freeze (at the time in `state.md`)
- Announce it. Tag `demo-safe-final`. From here: bug fixes on the demo path, polish of what the judge sees, and the pitch. **No new features.** If the user wants to add one, state the risk once in a sentence and ask them to confirm.
- Next: `hack-pitch`.
