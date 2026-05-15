---
title: "Schrödinger Equation"
date: 2020-07-24
type: research
category: "Physics/quantum-mechanics"
tags: [physics, quantum-mechanics, wave-function, schrodinger]
status: incomplete
source: "Notion Knowledge DB, tagged Physics; Wikipedia: Schrödinger equation"
related: [quantum-entanglement]
---

# Schrödinger Equation

Research stub on the central equation of non-relativistic quantum mechanics. Original Notion page was a brief gloss — expanded here into a proper note.

## The equation (time-dependent form)

```
iℏ · ∂Ψ/∂t = Ĥ Ψ
```

Where:

- `Ψ` (psi) is the **wave function** of the quantum system.
- `Ĥ` is the **Hamiltonian operator** (total energy: kinetic + potential).
- `ℏ = h / (2π)` is the reduced Planck constant.
- `i` is the imaginary unit.

## What the symbols mean

- **`Ψ` — wave function.** It encodes the probability amplitude for finding a particle at a given position and time. Because we genuinely *cannot know* where an electron is without measuring, the electron's state is "spread out" as a wave-like probability distribution.
- **`E` — energy eigenvalues.** The discrete energies an electron is allowed to have in a bound system. Related by Einstein's formula `E = hf` (energy proportional to frequency, with `h` the Planck constant).
- **`|Ψ|²`** — the **probability density** of finding the particle at a given location, per **Max Born's** statistical interpretation (1926). This reinterpretation is what made the wave function physically meaningful.

## Key ideas

1. **The wave function carries all information** about a quantum system. Everything measurable is derived from `Ψ`.
2. **Unitary, deterministic evolution.** Between measurements, `Ψ` evolves smoothly and deterministically according to the Schrödinger equation. Quantum weirdness enters only at measurement ("collapse").
3. **Born rule.** The probability of finding a particle in a small region is `|Ψ|²` integrated over that region. This is the bridge between the formalism and experiment.
4. **Time-independent form.** For stationary states, the equation reduces to `Ĥ ψ = E ψ` — an eigenvalue problem whose solutions are the allowed energy levels.

## Why it matters

- Explains the **discrete energy levels** of the hydrogen atom — the first big test, agreeing with spectroscopy.
- Underpins **chemistry** — molecular orbitals are Schrödinger-equation solutions.
- Foundation for **semiconductors, lasers, MRI, and virtually all quantum technology**.

## Related

- [[quantum-entanglement]] — entangled states are correlated wave functions that can't be factored into independent particle states.

## Open threads

- Write a derivation from the de Broglie hypothesis (wave-particle duality + classical wave equation).
- Work through the hydrogen-atom solution — a classic exercise.
- Contrast Schrödinger's formulation with Heisenberg's matrix mechanics (they're equivalent, but the mental models differ).

## References

- [Wikipedia — Schrödinger equation](https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation)

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/c6fda5c7e24a495bb0ee82053a5f00bd). See [[notion-migration]].*
