# Template: SaaS / Product Launch Film (15s & 30s)

A battle-tested blueprint for creating high-converting, premium product launch videos inspired by prompt-motion.com and modern SaaS brands (Linear, Raycast, Vercel, Supabase).

---

## 1. Core Structure & Narrative Arc (4-Beat Rhythm)

| Beat | Name | Duration (15s) | Duration (30s) | Objective & Visual Language |
| :--- | :--- | :---: | :---: | :--- |
| **Beat 1** | **The Hook** | 0.0s – 3.5s (0–105f) | 0.0s – 6.0s (0–180f) | Grab attention with a bold question, pain point, or category reframe. Giant display typography + floating category badge. |
| **Beat 2** | **The Chaos / Agitation** | 3.5s – 7.5s (105–225f) | 6.0s – 14.0s (180–420f) | Show the painful old way (scattered spreadsheets, manual messaging, lost fees) or introduce the core problem visually. |
| **Beat 3** | **The Platform Solution** | 7.5s – 11.5s (225–345f) | 14.0s – 24.0s (420–720f) | Clean UI showcase: window chrome, live counters, animated metric strip, interactive toggles, instant confirmations. |
| **Beat 4** | **The Unified Outro & CTA** | 11.5s – 15.0s (345–450f) | 24.0s – 30.0s (720–900f) | Vector brand mark, high-contrast headline, official domain card, CTA button, and 3-point trust row. |

---

## 2. Visual Rules (Anti-Slop Guardrails)

1. **Light Mode First (or Strict Editorial Dark):**
   - Light mode canvas: `#F8FAFC` or `#FFFFFF` with `#0B132B` ink.
   - Dark mode canvas: `#0A0A0C` or `#0F172A` with `#F8FAFC` ink.
   - **Banned:** Dull muddy greys, cheap neon gradients, purple-on-black AI clichés.

2. **Window Chrome Component:**
   - MacOS-style 3 dots (`#EF4444`, `#F59E0B`, `#10B981`) or minimalist border tabs.
   - Clean sub-pixel borders (`1px solid rgba(0,0,0,0.08)` or `border-slate-200`).
   - Deep smooth box-shadows (`0 25px 60px -15px rgba(0,0,0,0.12)`).

3. **Motion Transitions:**
   - **Continuous Flow:** Beat 2 morphs into Beat 3 via scale down, slide, or 3D card turn. Never cut to black or do a generic dissolve.
   - **Velocity Blur:** On elements moving faster than 800px/s, apply directional motion blur.

---

## 3. Remotion Implementation Pattern

```tsx
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';

export const SaasLaunchFilm: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Spring physics: Damping 12-14, Mass 0.8
  const hookSpring = spring({ frame, fps, config: { damping: 13, mass: 0.8, stiffness: 120 } });
  const cardScale = interpolate(hookSpring, [0, 1], [0.92, 1]);
  const cardOpacity = interpolate(hookSpring, [0, 0.4, 1], [0, 0.8, 1]);

  return (
    <AbsoluteFill style={{ backgroundColor: '#F8FAFC', fontFamily: 'Inter, Cairo, sans-serif' }}>
      {/* Dynamic Background Dot Grid */}
      <div style={{
        position: 'absolute', inset: 0,
        backgroundImage: 'radial-gradient(#CBD5E1 1.2px, transparent 1.2px)',
        backgroundSize: '32px 32px', opacity: 0.7
      }} />

      {/* Main Animated Stage */}
      <div style={{
        position: 'absolute', inset: 0,
        display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
        transform: `scale(${cardScale})`, opacity: cardOpacity
      }}>
        {/* Category Pill */}
        <div style={{
          padding: '8px 20px', borderRadius: 999, background: '#EFF6FF',
          border: '1.5px solid #BFDBFE', color: '#2563EB', fontWeight: 800, fontSize: 20
        }}>
          🚀 الجيل الجديد من إدارة المنصات
        </div>

        {/* Hero Punchy Headline */}
        <h1 style={{ fontSize: 56, fontWeight: 900, color: '#0F172A', textAlign: 'center', margin: '24px 0' }}>
          حوّل تدريسك إلى أكاديمية ذكية متكاملة
        </h1>
      </div>
    </AbsoluteFill>
  );
};
```
