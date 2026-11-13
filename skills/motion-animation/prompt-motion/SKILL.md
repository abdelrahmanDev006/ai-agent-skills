---
name: prompt-motion
description: Code-based AI motion graphics and video templates inspired by prompt-motion.com. Create high-converting SaaS product launch films, kinetic typography showreels, bento feature breakdowns, and comparison reels using Remotion (React) or deterministic HTML/Canvas with 120 BPM beat grids, spring physics, and anti-AI-slop design rules. Always activate when the user asks for motion graphics, video promos, reels, video templates, or code-to-video production.
---

# Prompt Motion (Code-Based Motion Graphics Engine)

A professional motion design and video engineering skill inspired by the 240+ curated code-to-video showreels on `prompt-motion.com`. It turns briefs and platform features into mathematically precise, studio-grade motion graphics videos rendered via **Remotion (React)** or deterministic **HTML/Canvas (`window.seek(t)`)**.

---

## 1. Core Philosophy: Deterministic Code vs Generative AI

Unlike diffusion video generators that produce blurry, morphing artifacts and hallucinations, **Prompt Motion** builds video through **code**:
* **100% Deterministic:** Every frame is rendered from pure code. Text is sharp, UI components are real vector elements, and coordinates are pixel-perfect.
* **Continuous Transformations:** Every scene is born out of the elements of the previous scene (shapes fold into cards, type morphs into geometry).
* **Beat-Grid Synchronization:** All motion events are locked to musical beats (e.g. 120 BPM = 1 beat every 15 frames at 30fps).

---

## 2. The 5 Master Video Templates

| Template | Duration | Best For | Visual Signature | Reference Guide |
| :--- | :---: | :--- | :--- | :--- |
| **1. SaaS Launch Film** | 15s – 30s | Product launches, platform releases, startup promos | Window chrome, metric strips, interactive toggles, animated counters | [template-saas-launch.md](references/template-saas-launch.md) |
| **2. Kinetic Showreel** | 15s | Brand statements, viral reels, agency portfolios | 120 BPM grid, variable font weight shifts (200→900), seamless looping | [template-kinetic-showreel.md](references/template-kinetic-showreel.md) |
| **3. Versus / Comparison** | 15s | High-converting B2B ads, switching campaigns | Red/slate chaos vs blue/emerald order, split screens, cost breakdowns | [template-versus-comparison.md](references/template-versus-comparison.md) |
| **4. Bento Feature Matrix** | 15s – 20s | Highlighting 3–4 complex features quickly | Modular 3D perspective cards, micro-interactions, live dashboard feeds | [template-saas-launch.md](references/template-saas-launch.md) |
| **5. Student & Security Reel** | 15s | Trust building, compliance, anti-piracy features | Floating watermarks, DRM locks, encrypted player simulation | [template-saas-launch.md](references/template-saas-launch.md) |

---

## 3. Anti-AI-Slop Guardrails (Strict Visual Rules)

To maintain world-class agency polish, the following patterns are **STRICTLY ENFORCED**:

### ❌ BANNED (AI Clichés & Cheap Defaults):
* **No cheap particle bursts, floating bokeh balls, or star sparks.**
* **No generic rainbow gradients** or random purple-on-black AI themes.
* **No artificial camera shake** or RGB chromatic split.
* **No lazy crossfades or cuts to black.** Elements must translate, scale, or morph.
* **No static holds longer than 0.5s (15 frames).** Constant kinetic tension must be preserved.
* **No fake or hallucinated product features.** Every claim must map to real product capabilities.

### ✅ MANDATED (Studio Standards):
* **Color Discipline:** Maximum 3 primary colors (e.g., `#2563EB` Royal Blue, `#10B981` Emerald, `#0F172A` Slate) on a clean `#F8FAFC` or `#FFFFFF` canvas.
* **Typography:** Single variable typeface family (e.g. `Geist`, `Inter`, `Cairo`) with deliberate weight contrasts (`font-black` 900 vs `font-medium` 500).
* **Spring Physics:** All animations must use calibrated harmonic oscillator springs (`damping: 12-14`, `mass: 0.8`, `stiffness: 110`). See [motion-physics-springs.md](references/motion-physics-springs.md).
* **Sub-pixel Glass & Borders:** `border: 1.5px solid rgba(226, 232, 240, 0.8)`, `backdrop-filter: blur(16px)`, soft layered drop shadows.

---

## 4. The 4-Beat Arc Architecture (Standard 15s Reel)

```
0.0s ─────── 3.5s ─────── 7.5s ─────── 11.5s ─────── 15.0s
[   BEAT 1   ] [   BEAT 2   ] [   BEAT 3   ] [   BEAT 4   ]
   THE HOOK        THE PAIN     THE PLATFORM   UNIFIED OUTRO
 Bold Question   Old Way/Chaos  UI Demo/Metric  Logo+URL+CTA
 (Frames 0-105) (Frames 105-225)(Frames 225-345)(Frames 345-450)
```

1. **Beat 1 (The Hook):** Giant typography, punchy problem statement, pill tag.
2. **Beat 2 (The Friction / Context):** The cost of the old way, manual errors, or market gap.
3. **Beat 3 (The Solution):** Live platform UI simulation, real numbers, zero latency.
4. **Beat 4 (The Unified Outro):** Official vector brand mark, verified domain in monospace card, royal blue CTA button, 3-point trust row.

---

## 5. Workflow: From Brief to Rendered Video

When asked to create or iterate on a video:
1. **Identify the Core Objective:** Select the template type (SaaS Launch, Kinetic Showreel, Versus, or Bento).
2. **Ground in Real Truth:** Audit the platform's actual features and database models to ensure zero fake promises.
3. **Choreograph the 4 Beats:** Define exact frame ranges (`0-105`, `105-225`, `225-345`, `345-450` at 30fps).
4. **Implement Component:** Build as a Remotion composition in `src/` using `useCurrentFrame()`, `spring()`, and `interpolate()`.
5. **Render & Verify:** Execute `npx remotion render` with `--concurrency=4` and verify with `ffprobe` (1080x1920, 30fps, 15.00s).

---

## 6. How to Write a Prompt-Motion Style Brief

When the user asks for a prompt rather than direct code, structure it using the four prompt-motion XML tags:

```markdown
<direction>
A 15-second vertical (1080x1920) SaaS launch film. Concept: "Instant payouts and zero platform hold". Every shot transforms out of the previous one without cutting. Light mode canvas (#F8FAFC) with royal blue (#2563EB) accents. Single font family (Cairo).
Banned: glows, particle bursts, camera shake, RGB splits, crossfades, generic gradients.
</direction>

<structure>
120 BPM grid.
Beat 1 (0-3.5s): Hook question "طالبك بيدفع إزاي؟" with category badge.
Beat 2 (3.5-7.5s): Interactive payment modal with InstaPay and Vodafone Cash logos.
Beat 3 (7.5-11.5s): Instant deposit confirmation + live counter showing 1,000 EGP straight to bank.
Beat 4 (11.5-15s): Unified Outro with official logo, riwaq-academy.org card, and start button.
</structure>

<build>
1. Remotion component at 1080x1920, 30fps, 450 frames.
2. Spring physics on all card entries: damping 13, mass 0.8, stiffness 110.
3. Vector SVG icons only, zero external raster images.
</build>

<start>
Build the Remotion component directly and render the final MP4.
</start>
```
