# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Falken21/u-po-pu-say-what-actually-broke-a2c153b5-entry/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Falken21/u-po-pu-say-what-actually-broke-a2c153b5-entry/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

A make.fun entry for **Say What Actually Broke**: one line of error copy
that names the real failure instead of hiding behind "something went wrong".

## The error message

> Something went wrong: we pushed an update at 4:59 p.m. on a Friday and it ate your file. The undo button works. The developer has been found.

It works in three beats: it admits exactly what happened (a Friday-evening
deploy destroyed a file), it immediately reassures the user about the one
thing they care about (undo works), and it closes with accountability as
the punchline — the developer has been found.

## Run it

```sh
python3 main.py
```

This writes the line to `/output/entry.txt` (no trailing newline).
