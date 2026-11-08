# Recon: PennApps XXVII

_Researched 2026-11-08 from pennapps.com, past PennApps coverage, and search. Devpost pages blocked automated fetching, so **re-run `hack-recon` once the XXVII Devpost/rules page is live** (likely Jan 2027) and replace every item marked UNVERIFIED._

## Event facts
| Item | Value | Confidence |
|---|---|---|
| Dates | Feb 5–7, 2027 | High (pennapps.com) |
| Duration | 36 hours | High (FAQ) |
| Location | University of Pennsylvania, Philadelphia (Eastern Time) | High |
| Team size | 2–4, **or solo** | High |
| Prizes | "$25k in prizes", no breakdown published | High |
| Tracks | Sustainability, Entertainment, Healthcare, Edge AI, Fintech, Education | High |
| Sponsors | Jane Street, Citadel, D. E. Shaw, a16z, SpaceX, xAI | High |
| **Applications** | **Priority closes Dec 6, 2026**; regular closes Jan 6, 2027; decisions early Jan | High |
| Admission | Application-based, judged by organizers (PennApps has published how it grades applicants) | Medium |
| Submission platform | Devpost (all recent editions used it) | Medium, UNVERIFIED for XXVII |
| Pre-existing code rule | Unknown | UNVERIFIED: ask organizers |

## Judging rubric
PennApps has used the same four criteria for a decade (PennApps X 2014, XX 2019, Fall 2023):

| Criterion | Weight | What "5/5" looks like here |
|---|---|---|
| Originality | 25% (assumed equal) | Not something past PennApps winners or the cliché list already did; ideally newly possible this year |
| Technical difficulty | 25% (assumed equal) | Visible, nontrivial engineering: on-device inference, real-time systems, hardware, custom models/pipelines, not one API call |
| Polish | 25% (assumed equal) | Works live on the first try, clean UI, no dead buttons on the demo path |
| Usefulness | 25% (assumed equal) | A specific person with a real problem, clearly better off |

**Format (historical, UNVERIFIED for XXVII):** judges score projects at an expo/demo session on the last morning → finalists demo on stage in front of the full audience → top 3 overall, plus track prizes. Older rules stated that judges do not judge code quality or style. **So two different demos are needed: a 60–90s table version that you repeat many times, and a ~3 min stage version.**

## Judges and sponsors (inferred from the sponsor list; actual judges unannounced)
- **Jane Street / Citadel / D. E. Shaw (quant):** engineers who reward correctness, performance, and clean reasoning about tradeoffs. They will see through a toy "budgeting app". If targeting Fintech, show real data, real latency/accuracy numbers, and an honest evaluation.
- **a16z (VC):** "who is this for, why now, could this be a company?"
- **SpaceX:** hardware/systems/reliability culture. Likely receptive to Edge AI and physical hacks.
- **xAI:** may offer an API-usage prize (UNVERIFIED). If so, deep integration beats a wrapper.

## Prize tracks to plausibly target
| Track | Fit notes | Competition guess |
|---|---|---|
| Edge AI | Highest technical-difficulty ceiling; on-device = visible depth; aligns with PennApps' hardware-winner history | Medium (harder to do, so fewer strong entries) |
| Fintech | Judged by quant engineers (likely). High bar, but few teams meet it | Medium |
| Healthcare | Usefulness is easy to argue; crowded with clichés | High |
| Sustainability | Was sponsor-backed last edition (Bloomberg) | High (carbon-tracker cliché pile) |
| Education | Crowded (study-buddy / flashcard clichés) | High |
| Entertainment | Open-ended; wow-moment friendly | Medium |

## Past winners (pattern-match)
| Edition | Project | One-line | Why it likely won |
|---|---|---|---|
| 2012 | ScratchTable | (details not found) | |
| 2013 | Inventory (UC Berkeley) | Detects what's in your backpack | Physical, instantly understandable wow |
| XVII (2018) | Object-seeking robot | Robot that finds objects | Hardware + CV, very visible demo |
| XX (2019) | DeFake | Browser extension estimating whether a video is a deepfake (ML) | Timely (election year), ML depth, real use |
| XXVI (2025) | CarbonChain | 1st in the Bloomberg Sustainability track | UNVERIFIED (LinkedIn post only) |

**Patterns:** (1) timely problem + real ML depth + instantly understandable demo; (2) physical/hardware hacks over-index among winners; (3) single-sentence explainability ("detects deepfakes", "finds objects").

## Rules that constrain us
- Solo is allowed (confirmed). As a solo builder, compete against 2–4 person teams by depth, not breadth.
- **Pre-existing code: unknown.** Until confirmed, assume only public libraries and boilerplate are allowed, and keep this repo to process (no project code).
- Hardware: PennApps historically had a hardware lab. Confirm for XXVII before planning a hardware hack.

## Key insights that should change what we build
1. **Technical difficulty is probably weighted above its 25% in practice.** The sponsors are quant firms, SpaceX, and xAI, so the judging pool skews toward engineers. Make the hard part visible.
2. **Edge AI is the best solo-fit track:** it rewards depth over breadth, makes the "LLM wrapper" suspicion easy to rebut (it runs on device), and fits the hardware-winner pattern.
3. **The expo format means two demos.** Optimize the 60-second table demo first, because finalists are chosen from it.

## Unknowns: ask organizers (contact@pennapps.com) or check in January
- Pre-existing code policy
- Exact judging format, finalist count, stage-demo length
- Per-track prize amounts and which sponsor judges which track
- Hardware lab availability and checkout list
- Devpost link and video length limit
- Exact start time (to compute the phase clock)
