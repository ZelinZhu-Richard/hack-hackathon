---
name: hack-judge
description: Simulate the hackathon judging panel to red-team an idea, a build-in-progress, or a pitch. Use when choosing between ideas, at build checkpoints, before feature freeze, and after a pitch rehearsal. Scores against the event's actual rubric and returns the questions judges will ask and the biggest reason this would NOT win.
---

# hack-judge: adversarial judging panel

Input: whatever is being judged (idea pitches, `idea.md`, a demo script, a running app, a rehearsal transcript) plus `.hackathon/recon.md`.
Output: appended to `.hackathon/judging.md` with a timestamp and what was judged.

## Panel
Build one persona per real judge from `recon.md` (role, what they value). If judges are unknown, use:
1. **Senior engineer**: "what did you actually build vs. call an API for?" Rewards visible technical depth; punishes fakery.
2. **Product / sponsor judge**: "would a real user use this tomorrow? Did you use our tech meaningfully?"
3. **Investor**: "who exactly is this for, why now, why you?"
4. **Domain expert** for the problem area: "does this match how the domain actually works?"

## Independence
If the Agent tool is available, spawn **one subagent per judge in parallel**. Give each only the artifact, the rubric, and their persona, and **not** your opinion or the team's reasoning, so they aren't anchored. Otherwise, evaluate each persona in a separate pass and don't let earlier verdicts leak into later ones.

Each judge must return:
- Score per rubric criterion (0–10) with one-line justification
- First impression in the first 30 seconds (lean in / neutral / checked out)
- The 2 questions they would ask
- **The single biggest reason this does not win**

## Synthesis (you)
```markdown
## <timestamp>: judged: <what>
| Criterion (weight) | J1 | J2 | J3 | J4 | Weighted avg |
**Expected weighted score:** x/10
**Consensus weakness:** ...
**Cheapest fix with the biggest score gain:** ... (est. time: ...)
**Questions to prepare answers for:** ...
```

Be calibrated, not nice. A typical hackathon project lands at 5–6/10. Reserve 8+ for things that would plausibly win. If the cheapest fix doesn't fit the time remaining in `state.md`, say so and give the next-best fix that does.
