---
title: "Realtime note detection (rtmonoaudio2midi)"
date: 2022-01-08
type: literature
category: "audio/ml"
tags: [audio, midi, realtime, python]
status: captured
source: "https://www.notion.so/0eafa0e1ce8742828d6097f50b80eb02"
external: "https://github.com/aniawsz/rtmonoaudio2midi/blob/master/synth.py"
video: "https://www.youtube.com/watch?v=9boJ-Ai6QFM"
related: []
---

# Realtime note detection

Reference bundle for real-time monophonic audio → MIDI pitch detection. Source repo: `aniawsz/rtmonoaudio2midi` (Python). The Notion page combined a YouTube demo, a GitHub preview card for the repo, and a mention of a related project page.

## Links

- YouTube demo — [9boJ-Ai6QFM](https://www.youtube.com/watch?v=9boJ-Ai6QFM)
- GitHub — [aniawsz/rtmonoaudio2midi/synth.py](https://github.com/aniawsz/rtmonoaudio2midi/blob/master/synth.py)

## What it is

A small Python project that listens to monophonic audio input (e.g. humming, a single-voice instrument), estimates the fundamental pitch in real time, and emits MIDI notes. The `synth.py` module wires the pitch stream to an audio synth so you can hear the round-trip.

## Open threads

- Extract the pitch-detection algorithm (YIN? autocorrelation? something simpler?) into its own research note if it's worth understanding in detail.
- Note any latency / accuracy numbers if re-benchmarked locally.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/0eafa0e1ce8742828d6097f50b80eb02). See [[notion-migration]].*
