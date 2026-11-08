# What wins hackathons

These are heuristics drawn from judging rubrics, judges' and winners' write-ups, and common patterns. They are **not** derived from a dataset. Treat them as priors, and let `lessons.md` (your own evidence) override them.

## The core model

**Score = Σ (rubric weight × judge's impression of that criterion)**, and the impression forms in a 3–5 minute demo by a tired person who has already seen 20 projects that day.

Everything below follows from that.

## 1. The rubric is the objective function
- Find the actual criteria and weights (rules page, Devpost "Judging Criteria", ask organizers). Typical set: impact/usefulness, technical difficulty, originality, design/UX, presentation, use of sponsor tech.
- Know who the judges are. An engineer-judge rewards visible technical depth. A VC-judge rewards market + "why now". A sponsor-judge rewards deep use of their API.

## 2. The demo is the product
- The first 30 seconds decide whether the judge is leaning in. Open with a specific person and a specific pain, then show the thing working.
- **One "wow moment"**: something visibly surprising that happens on screen. Design the project backward from it.
- A live, end-to-end, narrow slice beats a broad, half-built platform. Breadth is invisible in 3 minutes; broken buttons are very visible.
- Hardcode / seed / mock anything **off** the demo path. Make everything **on** the demo path genuinely work. Judges who discover that the core is fake will punish it hard.

## 3. Make technical depth visible
- Judges can't see your code. Show the hard part: an architecture diagram, a live trace or log, latency numbers, "here's what the model sees".
- "Wrapper around an LLM API" is the default suspicion in 2025–26 events. Pre-empt it: show what *you* built (data pipeline, custom eval, agent loop, tooling, fine-tune, hardware, integration).

## 4. Specific beats general
- "Helps ER nurses at night triage handoffs" > "AI healthcare platform".
- A named user with a real quote (talk to someone during the event if you can) is worth more than market-size slides.

## 5. Avoid the cliché pile
Overrepresented at almost every event (needs a sharp twist to stand out): generic AI chatbot/assistant for X, study buddy / flashcard generator, mental-health journaling, carbon-footprint tracker, food-waste app, resume reviewer, "Tinder for X", accessibility app built without talking to any disabled users.

## 6. Prize-track stacking
- Sponsor prizes are often less contested than the grand prize. If a sponsor API fits *genuinely*, integrate it deeply and submit to that track.
- Don't bolt on 5 sponsors superficially; sponsor judges can tell.

## 7. Talk to humans early
- Mentors, sponsors, and organizers often tell you what they want to see if you ask. Ask in the first 10% of the event.

## 8. Execution discipline
- Walking skeleton first (end-to-end, ugly) → then depth on the wow moment → then polish.
- Feature freeze at ~75% of time. Rehearse the demo ≥3 times. Record a backup video before the live demo.
- Submit a draft early. Devpost deadlines are strict and portals lag at the deadline.

## 9. Presentation
- Memorable name + one-line pitch a judge can repeat to other judges in deliberation.
- Speak to the judge's criteria explicitly: "Technically, the hard part was…", "The impact is…".
