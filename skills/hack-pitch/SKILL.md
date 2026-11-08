---
name: hack-pitch
description: Build and rehearse the hackathon demo pitch. Use after feature freeze, when the user asks for pitch help, slides, a demo script, Q&A prep, or a backup demo video. Produces a timed script mapped to the judging rubric, slide outline, Q&A answers, and a rehearsal loop with hack-judge.
---

# hack-pitch: win the 3 minutes

Inputs: `idea.md`, `plan.md` (demo script v1), `recon.md` (format, time limit, judges), `judging.md`.
Output: `.hackathon/pitch.md`.

## Structure (scale to the actual time limit; default 3 min ≈ 400 spoken words at ~130 wpm)
| Segment | Time | Content |
|---|---|---|
| Hook | 0:00–0:20 | A specific person + their specific pain. A number or a short story. Not "In today's world…" |
| Demo | 0:20–2:00 | Live. Narrate what the judge should notice. Land the wow moment by ~1:00. |
| How it works | 2:00–2:30 | One architecture slide. Name the hard part explicitly ("the technically hard part was…"). |
| Impact + next | 2:30–2:50 | Who benefits, how much, what's next. Mention the sponsor tech by name if targeting a track. |
| Close | 2:50–3:00 | Name + one-line pitch, repeated. |

Rubric check: for each criterion in `recon.md`, point to the exact sentence in the script that earns it. If a criterion has no sentence, add one.

## Deliverables in `pitch.md`
1. **Full spoken script** with timings (word counts per segment).
2. **Slide outline** (≤ 5 slides: title, problem, [live demo], architecture, impact/team). Offer to generate them via the pptx skill or an artifact if the user wants.
3. **Q&A bank**: the questions from `judging.md` plus the standard ones ("Is this live or mocked?", "What's novel vs. just calling an API?", "How would this scale / make money?", "What would you do with another week?", "What was the hardest bug?"). Write ≤ 25-word answers.
4. **Demo-failure plan**: who says what if the live demo breaks. Switch to the backup video without apologizing for more than one sentence.

## Backup video
Record at feature freeze, before the live demo: screen capture of the full demo path, 60–120s, with voiceover or captions. It's also the submission video in most cases (check the length limit in `recon.md`).

## Rehearsal loop (≥ 3 rounds)
1. User delivers the pitch with a timer (or pastes a transcript / voice-memo transcription).
2. Run `hack-judge` on it.
3. Fix the top issue only. Repeat.
Track timing each round. Over time means cut, never speed up.

Next: `hack-submit`.
