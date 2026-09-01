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

A **pañcāṅga** is a traditional calendar built from the positions and cycles of the Sun and Moon. The word means “five parts.”

## The five parts

- **Vāra**: weekday.
- **Tithi**: lunar day, based on the Moon–Sun angular difference.
- **Nakṣatra**: the Moon's position in a division of the ecliptic.
- **Yoga**: a division based on the sum of the Sun's and Moon's positions.
- **Karaṇa**: half of a tithi.

Let λₘ be the Moon's longitude and λₛ the Sun's longitude. The basic tithi calculation is:

~~~
Δ = (λₘ - λₛ) modulo 360
tithi = floor(Δ / 12°) + 1
~~~

The basic nakṣatra and yoga divisions use 27 segments of 13°20′. A karaṇa divides a tithi into two 6° segments. These formulas describe the geometry; a working calendar also needs an astronomical ephemeris, a location, a time zone, a day-boundary rule, and a sidereal or tropical convention.

The system is interesting as applied angular measurement, but the calculations should be kept separate from claims about the social or religious meaning assigned to a result. Historical statements about [[SuryaSidhantam]] and the age of these methods need source-specific verification.

## Related

- [[tithi]]
- [[SuryaSidhantam]]
