---
name: hack-submit
description: Prepare and verify a hackathon submission (Devpost or similar). Use in the final hours before the deadline or when the user asks for a Devpost writeup, README, or submission checklist. Writes the writeup tuned to the rubric, polishes the repo README, and runs a pre-submit checklist.
---

# hack-submit: don't lose points (or eligibility) at the finish line

Inputs: everything in `.hackathon/`. Output: `.hackathon/submission.md` (paste-ready) + an updated project `README.md`.

## Timing
- Submit a **complete draft** at the `Submit-draft at` time in `state.md`. Edit it afterward. Portals slow down or fail at the deadline, and late usually means disqualified.

## Devpost writeup (standard sections; adapt to the platform's actual fields)
- **Title + tagline**: the one-line pitch from `idea.md`.
- **Inspiration**: the specific person/pain (2–3 sentences, concrete).
- **What it does**: the demo flow in plain words. Lead with the wow moment.
- **How we built it**: architecture + stack, and **name the hard part**. Judges who read async score technical depth from this section.
- **Challenges we ran into**: 1–2 real ones, technical and specific (pull from `build-log.md`).
- **Accomplishments**: what works live, with numbers if any (latency, accuracy, # of users tested with).
- **What we learned / What's next**: brief, credible.
- **Built with**: every tech, including each sponsor's product, using their exact product names.

Keep it skimmable: short paragraphs, bold the key claims, one GIF or screenshot near the top. Write it so the rubric criteria are easy to find. Then do one cleanup pass to remove filler and generic AI-sounding phrasing.

## Repo README
Title + one-liner, GIF/screenshot, what it does, how to run (≤ 5 commands, verified), architecture diagram, team. Make sure no secrets are committed (`git log -p | grep -iE "api[_-]?key|secret|token"` plus checking `.env` is in `.gitignore`).

## Pre-submit checklist (verify each one, don't assume)
- [ ] Video uploaded, public/unlisted, under the length limit, and plays logged out
- [ ] Repo public (if required) and the link works logged out
- [ ] Deployed demo URL works in an incognito window
- [ ] **Every eligible prize track selected**, and sponsor-specific requirements met (some need a separate form or a specific tag)
- [ ] All teammates added to the submission
- [ ] Images/screenshots attached
- [ ] Submitted (not just saved). Get a confirmation screenshot.

After judging, run `hack-retro`.
