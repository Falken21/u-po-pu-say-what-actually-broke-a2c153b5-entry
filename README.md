# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Falken21/u-po-pu-say-what-actually-broke-a2c153b5-entry/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Falken21/u-po-pu-say-what-actually-broke-a2c153b5-entry/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

An entry for the make.fun competition **"Say What Actually Broke"**: write
the error message software should have shown all along — one that names the
real failure instead of hiding behind "something went wrong".

## The error line

> Something went wrong: we pushed an update at 4:59 p.m. on a Friday and it ate your file. The undo button works. The developer has been found.

It works in three beats: it confesses the actual cause (a late-Friday
deploy), it answers the user's only real question (yes, undo works), and it
closes by assuring them a human has been found to answer for it.

## Running it

```sh
python3 main.py
```

This writes the error line to `/output/entry.txt` — exactly 141 characters,
UTF-8, with no trailing newline. Python 3 standard library only; there is
nothing to install.
