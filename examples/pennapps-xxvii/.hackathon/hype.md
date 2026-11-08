# Buzz audit: Hangup (trial run of hack-hype at plan stage)

Judges (from recon.md): quant engineers (Jane Street / Citadel / D. E. Shaw), SpaceX, a16z, xAI. They reward visible technical depth and numbers, and they will probe "is this live?".

| Candidate | Judge signal | Real value to demo | Cost (h) | Demo-path risk | (S×V)/C | Verdict |
|---|---|---|---|---|---|---|
| On-device inference (Whisper-tiny + 4-bit LLM, WebGPU) | 5 | 5 | 6 | high | 4.2 | **CORE**: it *is* the project; spike first |
| Eval harness (200 labeled call transcripts → F1) | 5 | 4 | 3 | none | **6.7** | **ADD**: quant judges love a real number |
| Observability / trace panel (per-stage ms, bytes sent = 0) | 4 | 4 | 2 | low | **8.0** | **ADD**: makes the depth and privacy visible |
| Local vector index of known scam scripts | 3 | 4 | 2 | low | **6.0** | **ADD**: "matches the IRS-arrest script" makes the alert explainable |
| Streaming / realtime | 4 | 5 | 0 | n/a | n/a | Already inherent (streaming ASR) |
| Privacy by design | 4 | 4 | 0 | n/a | n/a | Already inherent; *show it* with airplane mode |
| Family SMS alert | 2 | 2 | 1 | low | 4.0 | MOCK: seeded, labeled honestly |
| LoRA fine-tune on eval failures | 4 | 2 | 8 | med | 1.0 | ROADMAP (NEXT node) |
| Bank hold API | 3 | 1 | n/a | n/a | n/a | ROADMAP: no real API access this weekend |
| Agentic tool use / MCP | 2 | 1 | 3 | med | 0.7 | KILL: decoration, no value to this user |
| xAI cloud escalation | 3 | 1 | 2 | high | 1.5 | KILL: contradicts "zero bytes leave the phone" |
| Redis cache / queue | 1 | 0 | 2 | low | 0 | KILL |

**Chosen (solo cap = 3):** eval harness, trace panel, scam-script index. Total +7h, scheduled after the walking skeleton.

## Where each appears in the demo
1. Airplane mode on → play the scam call → red banner at "gift cards" (on-device + realtime + privacy)
2. Banner text cites the matched script (vector index)
3. Flip to the trace panel: per-stage ms, **0 bytes sent** (observability)
4. Architecture slide → metrics strip with the F1 from the eval harness (eval)

## Target metrics (NOT on the diagram until measured)
| Metric | Target | Measure with |
|---|---|---|
| Scam phrase → alert latency (p50) | < 3 s | trace panel timestamps over 20 runs |
| F1 on labeled calls | > 0.85 | eval harness |
| Bytes sent off-device | 0 | browser network tab / Little Snitch |
| Model footprint | < 1.5 GB | file sizes |

## Diagram
`architecture.json` → `architecture.svg` / `.png`. At plan stage: no metrics strip (nothing measured yet). Re-render at freeze with measured numbers, and run the honesty pass.
