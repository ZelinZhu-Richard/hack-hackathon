---
name: hack-hype
description: Make a hackathon project's stack read as cutting-edge and its architecture diagram look impressive, without faking anything. Use after hack-scope (to choose which buzz-worthy tech to genuinely add to the plan) and at feature freeze (to render the architecture diagram for the pitch, Devpost, and README). Runs a "buzz audit" scored against the actual judges, then renders an animated, dark-theme architecture graph from a JSON spec.
---

# hack-hype: buzz that survives "is this live?"

Inputs: `recon.md` (who judges), `idea.md`, `plan.md`, and the codebase if it exists.
Outputs: `.hackathon/hype.md`, `.hackathon/architecture.json`, `.hackathon/architecture.svg` + `.png`.

## The one rule
**Everything on the diagram and in "Built with" is either running, or visibly marked MOCK / NEXT.** Engineer judges ask "is this live?" and open the network tab. At events where sponsors are also recruiting (e.g. PennApps' quant firms), getting caught inflating is worse than having less buzz: it costs the prize *and* the impression on people you may want to work for. Fake buzz has negative expected value, while real buzz in its cheapest form is usually only a few hours of work.

## Step 1: Buzz audit
Inventory what the project actually does (read the code if it exists, otherwise `plan.md`). Then score candidates from the menu below **against this event's judges** (from `recon.md`):

| Candidate | Judge signal (0–5) | Real value to the demo (0–5) | Cost (h) | Demo-path risk | **(signal × value) / cost** |

Pick the **top 2–4**. Kill anything with value ≤ 1 (pure decoration) or that puts the wow moment at risk. Solo: max 3, and none may push the walking-skeleton checkpoint.

### Menu (2026). Each item has a cheapest honest version
| Buzz | Cheapest real version | Signal to |
|---|---|---|
| On-device / edge inference | Quantized small model via ONNX Runtime Web / WebGPU / llama.cpp / Core ML; show "airplane mode" in the demo | Engineers, Edge AI tracks |
| Eval harness | 30–50 hand-labeled examples + a script that prints accuracy/F1. Put the number on the slide | Quant/ML engineers (very high) |
| Streaming / realtime | SSE or WebSocket token/event stream; show latency live | Engineers |
| Agentic tool use / MCP | A loop where the model calls 2–3 real tools you wrote; expose them as an MCP server | AI-sponsor judges |
| RAG + vector search | pgvector / Chroma over a *real* corpus that matters to the user; show retrieved sources | Product + AI judges |
| Observability panel | A live trace/log panel in the UI showing each pipeline stage + timing | Engineers (makes depth visible) |
| Structured outputs + validation | JSON-schema'd model outputs with retries; show a rejected/repaired example | Engineers |
| Voice / multimodal | Realtime STT/TTS or a camera input on the demo path | Everyone (wow) |
| Fine-tune / distill | LoRA on a few hundred examples, compared to base on your eval harness | ML judges |
| Privacy by design | Data never leaves the device; show it (network tab empty) | Healthcare/fintech judges |
| Caching / queueing | Redis cache with hit rate shown; job queue for slow tasks | Infra engineers |
| Sponsor API | Deep use of their product on the demo path (not a logo) | That sponsor's track |

Write the result to `hype.md` (table + chosen items + where each appears in the demo), and add the chosen items to `plan.md` with hours, **below** the walking-skeleton checkpoint.

## Step 2: Architecture spec
Write `.hackathon/architecture.json` (format documented at the top of `~/.claude/hack-hackathon/scripts/archgraph.py`). Design rules for a diagram that looks cool and reads in 5 seconds:
- **3–5 lanes** that tell a story left → right (e.g. `Device → Edge → Cloud → Data`, or `Input → Understand → Decide → Act`). Give lanes a short `sub` caption (e.g. "never leaves the phone").
- **≤ 14 nodes.** Each one gets a 2–4 word label and a concrete `sub` (model name, rate, size: "Whisper-tiny · int8", not "AI module").
- **Exactly one `hot` node**: the hard part you'll talk about. It glows.
- **Number the demo path** with `step` on edges, 1…n, matching the order you narrate in the pitch ("the audio goes 1 → 2 → 3…"). Demo edges animate.
- `status`: `live` (runs now), `mock` (seeded/faked for the demo, honestly labeled), `roadmap` (≤ 3 nodes; reads as vision).
- `metrics`: 3–4 **measured** numbers (latency, accuracy on your eval set, model size, cost per request). The renderer refuses metrics without `"measured": true`. At plan stage, use targets in `hype.md`, not on the diagram.

## Step 3: Render, look at it, iterate
```bash
python3 ~/.claude/hack-hackathon/scripts/archgraph.py .hackathon/architecture.json -o .hackathon/architecture.svg
node ~/.claude/hack-hackathon/scripts/svg2png.js .hackathon/architecture.svg
```
Then **look at the PNG** (Read the image) and fix crowding: long labels, too many nodes in one lane, crossing back-edges. Re-render. Two rounds is usually enough.

## Step 4: Honesty pass (at feature freeze, before submitting)
For every node: open the code path or run it. If it doesn't run, change it to `mock`/`roadmap` or delete it. "Built with" on Devpost lists only `live` and `mock` components (mock = you built the seeded version). Re-render.

## Where the outputs go
- Pitch: the "how it works" slide (the SVG animates in a browser-based deck; use the PNG elsewhere)
- Devpost: the PNG as the 2nd image, after the hero screenshot/GIF
- README: under "Architecture"
- Q&A: the numbered demo path *is* your answer to "walk me through how it works"
