# Portfolio Color Palette

Design tokens for the portfolio site. Use these names when adding CSS variables or Tailwind theme extensions.

---

## Backgrounds

| Token | Hex | Usage |
|-------|-----|-------|
| `background` | `#120D08` | The page itself. Every page, every section. |
| `background-deep` | `#0D0904` | The right hero panel and the canvas behind the animation. |
| `surface` | `#1A1208` | Cards, dropdowns, any element that floats above the page. |
| `surface-navy` | `#0F1C2E` | Project cards, Experience section bands, nav on scroll. |
| `surface-navy-raised` | `#1D2E44` | Hover state on navy cards. Border color for navy surfaces. |

---

## Text

| Token | Value | Usage |
|-------|-------|-------|
| `text-primary` | `#EDE0C8` | Your name, section headings, anything users must read. |
| `text-secondary` | `#EDE0C8` at 42% opacity | Body paragraphs, nav links default, card descriptions. |
| `text-muted` | `#EDE0C8` at 18% opacity | Scroll hints, timestamps, version labels, placeholder text. |

---

## Accent — Gold

| Token | Hex | Usage |
|-------|-----|-------|
| `accent` | `#C4956A` | Eyebrow labels, italic name, logo ∞, CTA button borders, animation center dot. |
| `accent-soft` | `#C4A86A` | Dashed rings, scroll ∞ suffix, decorative marks. **Never interactive.** |
| `accent-dim` | `#8B6A3A` | Divider lines, card border strokes, disabled/inactive states. |

---

## Accent — Navy

| Token | Value | Usage |
|-------|-------|-------|
| `accent-navy` | `#8BA8C4` | Tech stack tags, secondary CTAs, skill labels, active nav indicator. |
| `accent-navy-dim` | `#2C4A6A` | Selected/active state borders on navy cards. Tag backgrounds. |
| `border-navy` | `#8BA8C4` at 8% opacity | Nav hairline border. Any structural line that should barely exist. |

---

## CSS variables (reference)

Copy into `index.css` or Tailwind theme when wiring the design system:

```css
:root {
  /* Backgrounds */
  --background: #120D08;
  --background-deep: #0D0904;
  --surface: #1A1208;
  --surface-navy: #0F1C2E;
  --surface-navy-raised: #1D2E44;

  /* Text */
  --text-primary: #EDE0C8;
  --text-secondary: rgba(237, 224, 200, 0.42);
  --text-muted: rgba(237, 224, 200, 0.18);

  /* Accent — Gold */
  --accent: #C4956A;
  --accent-soft: #C4A86A;
  --accent-dim: #8B6A3A;

  /* Accent — Navy */
  --accent-navy: #8BA8C4;
  --accent-navy-dim: #2C4A6A;
  --border-navy: rgba(139, 168, 196, 0.08);
}
```
