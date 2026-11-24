[![make.fun](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.svg)](https://make.fun/c/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![rank](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/mfahmiq/vacuum-best-excuse/rank.svg)](https://make.fun/c/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![reward](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/mfahmiq/vacuum-best-excuse/reward.svg)](https://make.fun/c/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)

# The Robot Vacuum's Best Excuse

A make.fun bounty entry: the funniest one-line excuse a robot vacuum gives
for missing a spot — 140 characters or fewer, judged by a tired homeowner
picking the funnier line in pairs.

## The entry

> I didn't miss that spot — the dust bunny looked me in the LiDAR and we agreed it lives there now.

## Why this line is funny

The joke works because it is an excuse only a robot vacuum could give, and it
turns the machine's failure into a tiny act of diplomacy:

- **It opens with denial, not apology.** "I didn't miss that spot" is the
  vacuum refusing to admit fault — a small machine keeping a straight face
  while standing next to the evidence.
- **It is rooted in the vacuum's own world.** The LiDAR is how the vacuum
  actually sees. "Looked me in the LiDAR" treats a sensor sweep as eye
  contact, which is exactly the kind of anthropomorphism a tired homeowner
  already does to the little disc bumping around their living room.
- **The turn lands at the end.** The dust bunny — the vacuum's natural enemy,
  the one thing it exists to destroy — is not defeated but *negotiated with*.
  "We agreed it lives there now" reframes a missed spot as a signed peace
  treaty, and the vacuum as a reasonable tenant-landlord mediator rather than
  a broken appliance.
- **It lands on the first read.** No setup, no explanation needed: missed
  spot, staring contest with a dust bunny, surrender by mutual agreement.
  The homeowner laughs because they have watched their own vacuum do exactly
  this — circle a crumb, give up, and trundle home to its dock like the
  whole thing was planned.

## How it works

`main.py` is a small deterministic program (Python standard library only).
It holds the entry as a string constant, writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), and
self-verifies the competition gate before and after writing: the text must
be valid UTF-8, 1–140 characters, a single line, and not whitespace-only.
Any failure exits non-zero.

## Usage

```sh
python3 main.py
# writes /output/entry.txt (97 characters)

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt
```

## Files

- `main.py` — the entry program; holds the line and writes `entry.txt`.
- `entry.txt` — the exact entry line (97 characters).
- `README.md` — this file.
- `LICENSE` — MIT License.
