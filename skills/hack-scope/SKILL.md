---
name: hack-scope
description: Turn the chosen hackathon idea into a time-boxed build plan by working backward from the demo. Use after hack-ideate picks an idea. Writes the demo script first, derives the minimum build that makes it real, assigns owners, sets hourly checkpoints and a cut list, and writes .hackathon/plan.md.
---

# hack-scope: plan backward from the demo

Inputs: `idea.md`, `recon.md`, `state.md`. Output: `.hackathon/plan.md`. Time box: ~3% of event time.

## Step 1: Write the demo script FIRST
Write the 2-minute demo as a click-by-click, line-by-line script: what's on screen, what the presenter says, what the judge should feel. Mark the **wow moment**. This script is the spec. Anything not in it is optional.

## Step 2: Classify every component on the demo path

| Component | In demo? | Must be REAL | Can be faked/seeded | Owner | Est. hours |

- **Real**: anything a judge might poke at or ask "is this live?" about, and the wow moment itself.
- **Fake/seed**: login, settings, onboarding, pagination, admin, multi-tenant, payments, and any screen shown for under 3 seconds.
- Default stack choice: whatever the team already knows best. A hackathon is not the time to learn a framework unless that's a sponsor requirement.
- Sum the estimates and multiply by **1.5** (hackathon estimates are optimistic). If the total exceeds the build budget in `state.md`, cut now, not at 3am.

## Step 3: Architecture sketch
A ~10-line diagram (ASCII or mermaid) of the components and data flow. It doubles as the "how it works" slide later. Identify the **riskiest integration** (a new API, a model, hardware, or auth to a third party) and schedule a 30-minute spike on it **first**.

## Step 4: Plan with checkpoints

```markdown
# Build plan: <project>
## Demo script (v1)
## Architecture
## Riskiest unknown → spike first: <what>, by <time>
## Checkpoints (absolute times)
- <T1> Spike done: risky integration proven or pivot to fallback
- <T2> Walking skeleton: demo path runs end-to-end (ugly, hardcoded OK)
- <T3> Wow moment works 5/5 times
- <T4> FEATURE FREEZE: tag `demo-safe`
## Owners
## Cut list (in cut order: first item gets dropped first when behind)
## Fallbacks (if API/model X fails live: cached response / recorded clip / local model)
```

Each checkpoint has a **pivot rule**: e.g. "if the spike isn't working by T1, switch to the runner-up approach in idea.md". Write it down now, while calm.

Log in `state.md`. Next: `hack-build`.
