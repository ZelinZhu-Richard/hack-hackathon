---
name: hack-ideate
description: Generate, score, and select a hackathon idea against the event's judging rubric. Use after hack-recon, or when the user is brainstorming hackathon ideas. Produces many candidates, kills weak ones with explicit rules, runs hack-judge on finalists, and writes .hackathon/idea.md.
---

# hack-ideate: choose the idea that maximizes expected score

Inputs: `.hackathon/recon.md`, `.hackathon/state.md`, `~/.claude/hack-hackathon/playbook/principles.md` and `lessons.md`.
Output: `.hackathon/idea.md`. Time box: ≤ 5% of event duration (≤ 30 min for short events).

## Step 1: Diverge (aim for 15–25 raw ideas, fast)
Generate from several angles so the ideas aren't all the same shape:
- **Sponsor-first**: what's the most impressive thing you could do with each sponsor API?
- **Judge-first**: what would make each specific judge lean forward?
- **Unfair advantage**: what do the team's skills, data, or access make uniquely easy for us?
- **Wow-moment-first**: what's a visibly surprising 10-second moment? Work backward to a product.
- **Specific-person-pain**: a named type of person with a pain they'd pay to remove.
- **Recent capability**: something that became possible in the last ~6 months (new model, API, hardware) that past winners couldn't do.

Ask the user for their own ideas too, and include them unjudged in the pool.

## Step 2: Kill rules (apply before scoring, and say which rule killed what)
- Core demo path can't run end-to-end by ~35% of event time → out
- Needs data, access, or hardware we don't have and can't get today → out
- On the cliché list in principles.md with no sharp twist → out
- Substantially the same as a past winner of this event → out
- Violates a rule in recon.md → out

## Step 3: Score the survivors (0–5 each, show the table)

| Idea | Rubric fit (weighted per recon) | Wow in 30s | Feasibility | Novelty | Track stack | Team fit | **Total** |

- Rubric fit uses the actual weights from recon.md and counts double.
- Feasibility = confidence the wow moment works reliably *live* by freeze time.
- Be harsh. If everything scores 4+, you aren't discriminating.

## Step 4: Finalists → judge panel
Take the top 3. For each, write a 3-sentence pitch (who / pain / the wow moment). Run `hack-judge` on all three (it simulates the actual judges). Pick the winner by **expected score**, accounting for execution risk, not by which idea is most exciting to build.

If the team strongly prefers an idea that scored lower, say so plainly with the numbers, then defer to them. Motivation matters for a 24h build, and it's their call.

## Step 5: Write `.hackathon/idea.md`

```markdown
# <Project name>: <one-line pitch a judge could repeat>
## User + pain
## The wow moment (what the judge sees, second by second)
## Why it scores (map to each rubric criterion)
## Prize tracks targeted
## Biggest risks + mitigation
## Runner-up idea (fallback if we pivot by <time>)
```

Log the decision in `state.md`. Next: `hack-scope`.
