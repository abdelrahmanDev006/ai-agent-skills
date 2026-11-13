# Motion Physics: Springs & Easing Reference

To eliminate the "cheap robotic AI" look, animations must obey physical laws: mass, tension, and damping.

---

## 1. Remotion Spring Presets

Use `spring()` from Remotion with calibrated presets:

```typescript
import { spring } from 'remotion';

// 1. Natural UI Entry (Best for Cards, Modals, Windows)
// Smooth deceleration, zero jitter, micro overshoot (<2%)
export const SPRING_UI_NATURAL = {
  damping: 14,
  mass: 0.8,
  stiffness: 110,
};

// 2. Snappy Badge & Counter Pop (Best for Numbers, Badges, Checkmarks)
// Fast attack, lively snap
export const SPRING_POP_SNAPPY = {
  damping: 11,
  mass: 0.6,
  stiffness: 160,
};

// 3. Heavy Architectural Anchor (Best for Background Panels, Fullscreen shifts)
// Slow, weighty, stable
export const SPRING_HEAVY_ANCHOR = {
  damping: 20,
  mass: 1.5,
  stiffness: 85,
};
```

---

## 2. Pure JavaScript Spring Function (For HTML Canvas / window.seek(t))

When rendering without Remotion (pure HTML/JS timeline):

```javascript
// Damped Harmonic Oscillator function of time t (seconds)
export function solveSpring(t, { mass = 1, stiffness = 100, damping = 10 } = {}) {
  const omega0 = Math.sqrt(stiffness / mass);
  const zeta = damping / (2 * Math.sqrt(stiffness * mass));

  if (zeta < 1) {
    // Under-damped (oscillates smoothly before settling)
    const omegaD = omega0 * Math.sqrt(1 - zeta * zeta);
    const envelope = Math.exp(-zeta * omega0 * t);
    return 1 - envelope * (Math.cos(omegaD * t) + (zeta * omega0 / omegaD) * Math.sin(omegaD * t));
  } else {
    // Critically damped or over-damped
    return 1 - Math.exp(-omega0 * t) * (1 + omega0 * t);
  }
}
```

---

## 3. Directional Motion Blur Rule

When an element moves $> 600px$ per second across the viewport, standard digital animation appears stroboscopic.
Simulate camera shutter exposure with CSS backdrop-filter or SVG gaussian blur:

```css
/* Inline dynamic blur based on frame delta */
filter: blur(calc(abs(var(--velocity-x)) * 0.08px));
```
