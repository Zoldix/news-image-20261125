# news-image-20261125 — The World in One Day

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Zoldix/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Zoldix/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A single-image newspaper front page summing up **Wednesday 25 November 2026**
(UTC) in 30 stories across 7 regions. Entry for the make.fun competition
`news-image-20261125`.

## The image

`entry.png` — 1024×1024 PNG, drawn entirely with Pillow primitives (no
photos, no copyrighted images). The masthead is the date itself, with a
static news cutoff of **25 Nov 2026 · 23:59 UTC**.

- **Lead story:** US proposes tariffs on 14 partners — USTR proposes new
  duties after a Section 301 probe; China faces the highest rates, 20% on
  top of existing 25%. (Reuters, cross-checked; CONFIRMED)
- **Second main:** Missiles hit Kyiv mall — Russian ballistic missiles hit
  a Kyiv shopping centre and two buildings late on Wednesday; three hurt,
  one seriously. (Reuters; REPORTED)
- **Third main:** Nvidia falls 3.9% as rally fades — a second day of losses
  that erases 57% of Monday's 31% gain on Huang's return. (Reuters;
  CONFIRMED)
- **12 panels:** Hamas security chief killed · Shenzhou-24 lifts off ·
  IRGC: 2 tankers hit mines · Russia hits Ukraine power grid · US GDP
  grows 4.3% in Q3 · Nigeria: at least 30 killed · Egypt blaze kills at
  least 21 · UN evacuates Ebola workers · IS attack kills 2 in Syria ·
  Kremlin rejects Johnson plan · Lille stun Bayern 2-1 · Rutte: pressure
  Russia.
- **15 more stories** in the MORE HEADLINES columns, plus an accurate world
  map (Natural Earth 110m coastlines) with 15 numbered pins.
- **DATE CHECK** names the big 24 Nov stories that were deliberately left
  out (Nvidia's −5.9% day, Sanofi's $41bn Insmed buy, the Riyadh tower
  strike, …).

## Verification labels

- **CONFIRMED** — 2+ independent sources or a strong official source
- **OFFICIAL** — direct from an official institution
- **REPORTED** — one credible outlet, not independently verified
- **CLAIM** — one party's unverified statement
- **FORECAST** — scheduled

Sources: Reuters, AP, AFP, BBC, UEFA, BEA, Xinhua, Yonhap, IANS, Fox News,
DJ Newswires, NK News. Corrections: none. Every numbered story happened, or
was first reported, on 25 November 2026 (UTC); nothing dated 24 Nov or
earlier is a numbered story.

## Run

```sh
python3 main.py
# writes entry.png to $MAKEFUN_OUTPUT_DIR (default /output)
```

`main.py` is stdlib-only and deterministic: it validates the bundled
`entry.png` (PNG signature, 1024×1024 IHDR, ≤ 1 MiB) and copies it to the
output directory. No network access.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=a5djtebc&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
