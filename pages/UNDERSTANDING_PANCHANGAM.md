---
title: "Understanding Panchangam"
date: "2026-05-05"
type: "research"
category: "Legacy/Pages"
tags: ["panchanga", "astronomy", "calendar", "jyotisha"]
status: "draft"
related: ["[[tithi]]", "[[SuryaSidhantam]]"]
---

# Understanding Panchangam

పంచాంగం = five limbs: Vāra, [[tithi]], Nakṣatra, Yoga, Karaṇa.
Two inputs. Sun longitude λₛ, Moon longitude λₘ. Everything else is geometry.

<img src="../assets/Screenshot_2026-01-03_at_10.05.02 PM_1767508045762_0.png" alt="Screenshot 2026-01-03 at 10.05.02 PM.png" width="100%" />

<img src="../assets/EclipticScene_ManimCE_v0.19.1_1767508813101_0.gif" alt="EclipticScene_ManimCE_v0.19.1.gif" width="100%" />

## Two clocks

- Ecliptic = Sun's yearly path. Tilted 23.4° to the celestial equator. All angles are measured along it.
- Sun = slow hand. 360° / 365.25 d ≈ 1°/day.
- Moon = fast hand. 360° / 27.3 d ≈ 13.2°/day.
- Moon gains 12.2°/day on Sun → 360° / 12.2 ≈ 29.53 days = synodic month (New Moon to New Moon).
- Synodic > sidereal because the Moon has to catch a Sun that moved ~30°.

```text
normalize(θ) = ((θ mod 360) + 360) mod 360
Δ = normalize(λₘ - λₛ)    # difference → phase
Σ = normalize(λₘ + λₛ)    # sum → yoga
```

| Δ    | Phase         |
| ---- | ------------- |
| 0°   | New Moon      |
| 90°  | First Quarter |
| 180° | Full Moon     |
| 270° | Last Quarter  |

## Tithi = Δ in 12° steps

```text
T = floor(Δ / 12°) + 1        T ∈ 1..30
Δ = 47° → floor(3.917) + 1 = 4
```

- Shukla paksha: T 1–15, Δ ∈ [0°, 180°), waxing.
- Krishna paksha: T 16–30, Δ ∈ [180°, 360°), waning.
- Average tithi = 29.53 / 30 ≈ 23.6 h. Not constant: orbit is elliptical (Kepler 2).
- Perigee ~15.5°/day → tithi ~19h 59m. Apogee ~11.5°/day → tithi ~26h 47m.

## Nakṣatra = Moon alone in 13°20′ steps

```text
N = floor(λₘ / 13.333°) + 1   N ∈ 1..27
λₘ = 45° → 4 → Rohini
Pada: P = floor((λₘ mod 13.333°) / 3.333°) + 1   P ∈ 1..4
27 × 4 = 108 padas
```

Why 27? Sidereal month ≈ 27.3 days. One mansion per night.

1 Ashwini · 2 Bharani · 3 Krittika · 4 Rohini · 5 Mrigashira · 6 Ardra · 7 Punarvasu · 8 Pushya · 9 Ashlesha · 10 Magha · 11 Purva Phalguni · 12 Uttara Phalguni · 13 Hasta · 14 Chitra · 15 Swati · 16 Vishakha · 17 Anuradha · 18 Jyeshtha · 19 Mula · 20 Purva Ashadha · 21 Uttara Ashadha · 22 Shravana · 23 Dhanishtha · 24 Shatabhisha · 25 Purva Bhadrapada · 26 Uttara Bhadrapada · 27 Revati

## Yoga = sum in 13°20′ steps

```text
Y = floor(Σ / 13.333°) + 1    Y ∈ 1..27
dΣ/dt ≈ 13.2 + 1.0 = 14.2°/day → 13.333 / 14.2 ≈ 0.94 d ≈ 22.5 h
```

1 Vishkumbha · 2 Priti · 3 Ayushman · 4 Saubhagya · 5 Shobhana · 6 Atiganda · 7 Sukarma · 8 Dhriti · 9 Shula · 10 Ganda · 11 Vriddhi · 12 Dhruva · 13 Vyaghata · 14 Harshana · 15 Vajra · 16 Siddhi · 17 Vyatipata · 18 Variyan · 19 Parigha · 20 Shiva · 21 Siddha · 22 Sadhya · 23 Shubha · 24 Shukla · 25 Brahma · 26 Indra · 27 Vaidhriti

Vyatipata, Vaidhriti → avoided for important work.

## Karaṇa = half tithi, 6° steps

```text
K = floor(Δ / 6°) + 1         K ∈ 1..60
Fixed:    K=1 Kimstughna · K=58 Shakuni · K=59 Chatushpada · K=60 Nagava
Rotating: K=2..57, 8 rounds of
          Bava → Balava → Kaulava → Taitila → Gara → Vanija → Vishti
          index = (K - 2) mod 7
```

Vishti (Bhadra) comes 8 times a month. Avoided for beginnings.

## Vāra = weekday

```text
V = (Julian Day Number + 1) mod 7
0 Ravi (Sun) · 1 Soma (Moon) · 2 Mangala (Mars) · 3 Budha (Mercury)
4 Guru (Jupiter) · 5 Shukra (Venus) · 6 Shani (Saturn)
```

- Order comes from Hora: 24 planetary hours, planets in order Saturn → Jupiter → Mars → Sun → Venus → Mercury → Moon. Start Saturday at Saturn; 25th hour = Sun → Sunday.
- Day changes at sunrise, not midnight. So location matters.

## Worked example

```text
Given: 15 Jan 2025, 12:00 UTC, JD = 2460691.0
λₛ (sidereal) = 270.67°   λₘ (sidereal) = 63.24°

Δ = normalize(63.24 - 270.67) = normalize(-207.43) = 152.57°
Σ = normalize(63.24 + 270.67) = 333.91°

Tithi     floor(152.57 / 12) + 1     = 13 → Shukla Trayodashi
Nakshatra floor(63.24 / 13.333) + 1  = 5  → Mrigashira
Yoga      floor(333.91 / 13.333) + 1 = 26 → Indra
Karana    floor(152.57 / 6) + 1      = 26 → (26-2) mod 7 = 3 → Taitila
Vara      (2460691 + 1) mod 7        = 3  → Budhavara (Wednesday)
```

(is this right ? Pausha Purnima was 13 Jan 2025, so 15 Jan should be Krishna paksha. The λ values look made up. Arithmetic is fine; inputs need a real ephemeris.)

## Sidereal vs tropical

- Equinox drifts ~50″/year (precession, ~26,000-year cycle) → ~1° every 72 years.
- Tropical zodiac is tied to the equinox. Sidereal is tied to the stars.
- λ_sidereal = λ_tropical − Ayanamsa. Lahiri, 2025 ≈ 24.2°.
- Ephemeris gives tropical. Panchangam needs sidereal. Convert first.

## Edge cases

- Tithi kshaya: tithi starts after one sunrise and ends before the next. Never rules a sunrise. Skipped.
- Adhika tithi: long tithi spans two sunrises. Rules two days.
- Same UTC instant → different panchangam in different cities. Need location, time zone, sunrise rule.

## Reference

| Element   | Per month | Step    | Avg duration |
| --------- | --------- | ------- | ------------ |
| Tithi     | 30        | 12°     | 23.6 h       |
| Nakshatra | 27        | 13°20′  | 24.3 h       |
| Yoga      | 27        | 13°20′  | 22.5 h       |
| Karana    | 60        | 6°      | 11.8 h       |

Nesting: Tithi (12°) → Paksha (180°) → Masa (360°) → Samvatsara (60 years).

[[SuryaSidhantam]] values (verify against source): sidereal year 365.2588 d (modern 365.2564), synodic month 29.530583 d (modern 29.530589).
