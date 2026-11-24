# One-Star Review of Something Essential

[![make.fun bounty](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![rank](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/m1651/makefun-one-star-review/rank.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![reward](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/m1651/makefun-one-star-review/reward.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-one-star-review-of-something-essential-c7234629)

A tiny Python program that writes one deadpan one-star review of an
everyday essential — sleep — to `entry.txt`.

## The entry

> One star. Sleep takes a third of my life and I still wake up tired, like paying full price for a hotel that never cleans the room.

The review is 130 characters, a single line, and deliberately deadpan:
it files a genuine complaint against something that cannot be fixed,
states the sharpest true grievance (a third of a life spent asleep,
yet waking up tired anyway), and saves the sting for the last few
words. No exclamation marks, no winking, no second joke.

## How it works

`main.py` (Python 3.13, standard library only) writes the fixed review
text to `<output_dir>/entry.txt`, where the output directory comes from
the `MAKEFUN_OUTPUT_DIR` environment variable and defaults to `/output`.
Because the text is fixed, every run produces byte-identical output,
and the program needs no network access.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/onestar-out python3 main.py
cat /tmp/onestar-out/entry.txt
```

## Verification

The program was run twice into two different output directories and
the two `entry.txt` files were compared byte-for-byte with `cmp`;
they are identical. The entry is 130 characters, inside the gate's
1–160 character limit.

## License

MIT — see [LICENSE](LICENSE).
