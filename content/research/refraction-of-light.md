---
title: "Refraction of Light"
date: 2020-07-29
type: research
category: "Physics/optics"
tags: [physics, optics, refraction, snells-law]
status: incomplete
source: "Notion Knowledge DB, tagged Physics"
related: [sun]
---

# Refraction of Light

Short research stub on refraction — the bending of light as it passes from one medium to another. Originally one-liner in Notion; fleshed out here.

## The phenomenon

When a light ray crosses a boundary between two media with different optical densities, it changes direction. The classic visual example: a straw in a glass of water appears bent or displaced at the water line.

## Snell's Law

For a ray crossing from medium 1 (refractive index `n₁`) to medium 2 (refractive index `n₂`):

```
n₁ · sin(θ₁) = n₂ · sin(θ₂)
```

Where `θ₁` and `θ₂` are the angles from the normal (perpendicular to the boundary surface) in each medium.

## Why it bends

Light travels at different speeds in different media:

- **Vacuum**: `c ≈ 3 × 10⁸ m/s`.
- **Water**: roughly `c / 1.33`.
- **Glass**: roughly `c / 1.5`.

The refractive index `n = c / v` quantifies the slowdown. At a boundary, the wavefront — the surface of constant phase — has to stay continuous. If the ray hits at an angle and one side of the wavefront enters the slower medium first, that side slows down while the other side keeps going faster briefly, tilting the wavefront. Fermat's principle gives the same conclusion: light takes the path of least time.

## Consequences

- **Lenses** work via refraction — they bend incoming rays to converge at a focal point.
- **Prisms** split white light into a rainbow because `n` depends weakly on wavelength (**dispersion**). Blue light refracts more than red.
- **Atmospheric refraction** makes celestial objects appear slightly higher than their true positions — the sun you see at sunset has already set geometrically.
- **Mirages** — refraction through layered air of different temperatures — make distant objects shimmer or appear inverted.
- **Total internal reflection** — when going from a denser to less-dense medium above a critical angle, all light reflects back. The basis for **optical fibers**.

## Related

- [[sun]] — atmospheric refraction is why the sun appears higher than its geometric position near the horizon.

## Open threads

- Derive Snell's law from Fermat's principle of least time.
- Write a separate note on **total internal reflection** and optical fibers.
- Explore **dispersion** quantitatively — the Cauchy / Sellmeier equations for `n(λ)`.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/04308e74b9a0467d923a5dc3d92acd33). See [[notion-migration]].*
