# Template: Kinetic Typography & Motion Showreel (120 BPM)

Inspired by the top-ranked prompt on `prompt-motion.com` (used in 49+ viral motion showreels), this template creates an aggressive, high-energy showreel where typography, geometric shapes, and UI moments transform into one another seamlessly on every beat.

---

## 1. The 120 BPM Beat Grid Architecture

At 120 BPM (2 beats per second):
- **1 Beat** = 0.50 seconds = **15 frames** (at 30fps) or **30 frames** (at 60fps).
- **1 Bar** (4 beats) = 2.00 seconds = **60 frames** (at 30fps) or **120 frames** (at 60fps).
- **Total Duration (15s)** = 30 beats = 7.5 bars = **450 frames** (at 30fps).

### The Choreography

```
Bar 1 (0.0s – 2.0s):  THE HOOK. A single kinetic statement snaps onto the grid.
Bar 2 (2.0s – 4.0s):  KINETIC TYPE. Font weight ramps from 200 -> 900 while tracking shifts.
Bar 3 (4.0s – 6.0s):  SHAPE MORPH. The words fold inward and compress into geometric circles/squares.
Bar 4 (6.0s – 8.0s):  2D TO 3D MOMENT. Isometric card rotation with dynamic perspective (rotateX/rotateY).
Bar 5 (8.0s – 10.0s): UI / DATA MATRIX. Live counter rapidly incrementing with audio click ticks.
Bar 6 (10.0s – 12.0s): THE PEAK. The most explosive, high-density transform of the video.
Bar 7 (12.0s – 15.0s): END TITLE & LOOP. Resolves cleanly to the hero brand mark and domain.
```

---

## 2. The Strict Rules of Kinetic Typography

1. **One Typeface Family Only:**
   - Use variable fonts with wide weight ranges (e.g. `Geist`, `Inter`, `Cairo`, `Space Grotesk`).
   - Modulate `fontWeight: 300 -> 900`, `letterSpacing: -0.05em -> 0.05em`, and `fontSize` instead of switching fonts.

2. **No Fades, No Cuts:**
   - If a word leaves, it must:
     a) Scale into a zero-width slice,
     b) Get masked by a sliding container, or
     c) Morph its SVG path into the incoming shape.

3. **Motion Blur Simulation:**
   - When a word moves across > 400px within 6 frames, inject a dynamic `filter: blur(${speed * 0.15}px)` in the direction of motion.

---

## 3. Web Audio API Synthetic Beat Generator (Zero External Assets)

```javascript
// Programmatic 120 BPM beat track using browser OfflineAudioContext
export async function generateSyntheticBeatTrack(durationSeconds = 15, bpm = 120) {
  const sampleRate = 44100;
  const ctx = new OfflineAudioContext(2, sampleRate * durationSeconds, sampleRate);
  const beatInterval = 60 / bpm; // 0.5s for 120 BPM

  for (let time = 0; time < durationSeconds; time += beatInterval) {
    const isDownbeat = Math.round(time / beatInterval) % 4 === 0;

    // Synthesize Kick Drum on each beat
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.frequency.setValueAtTime(isDownbeat ? 140 : 100, time);
    osc.frequency.exponentialRampToValueAtTime(0.01, time + 0.12);

    gain.gain.setValueAtTime(isDownbeat ? 0.9 : 0.6, time);
    gain.gain.exponentialRampToValueAtTime(0.001, time + 0.12);

    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start(time);
    osc.stop(time + 0.12);
  }

  const renderedBuffer = await ctx.startRendering();
  return renderedBuffer; // Convert to WAV or play inline
}
```
