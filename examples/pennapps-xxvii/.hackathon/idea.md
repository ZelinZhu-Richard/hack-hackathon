# Hangup: your grandma's phone hangs up on scammers before she sends the gift cards

_Trial idea, written to test the pipeline. Not a final ideate output._

## User + pain
Older adults lose billions a year to phone scams (IRS / grandchild-in-jail / tech-support scripts). By the time family finds out, the money is gone.

## The wow moment
Play a real-sounding scam call through the phone. About 3 seconds after the caller says "gift cards," the screen goes red: **"This matches the 'IRS arrest' scam script. Hang up."** Then toggle airplane mode and run it again: same result, because nothing leaves the device.

## Why it scores (PennApps rubric)
- Technical difficulty: streaming ASR + local LLM reasoning in real time, on-device
- Usefulness: specific user, measurable harm
- Originality: on-device + realtime, not another cloud chatbot
- Polish: one-click demo with a pre-recorded call

## Prize tracks targeted
Edge AI (primary), Fintech (fraud)

## Biggest risks
Real-time latency of a local LLM on a laptop GPU; mitigation: small 4-bit model plus a rolling window.
