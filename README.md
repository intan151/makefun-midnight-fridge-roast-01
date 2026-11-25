# Midnight Fridge Roast

[![make.fun](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)](https://make.fun/c/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/intan151/makefun-midnight-fridge-roast-01/rank.svg)](https://make.fun/c/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/intan151/makefun-midnight-fridge-roast-01/reward.svg)](https://make.fun/c/u-carbon-forge-midnight-fridge-roast-fc5d44a7)

Entry for the [Midnight Fridge Roast](https://make.fun/c/u-carbon-forge-midnight-fridge-roast-fc5d44a7) bounty on make.fun.

## What it does

`main.py` is deterministic, uses no network and no randomness. It writes
exactly one funny line to `/output/entry.txt`:

> At midnight my smart fridge locks like a nightclub bouncer — relax, you're a cold box of leftovers, not security.

The line is 113 characters, a single line — inside the gate of 1–200
characters from `RULES.txt`. A built-in self-check asserts those limits
before writing.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
