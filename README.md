# Out of Office: The Overworked AI's Auto-Reply

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3](https://img.shields.io/badge/python-3-blue.svg)](main.py)
[![make.fun entry](https://img.shields.io/badge/make.fun-entry-brightgreen.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

Entry for the [make.fun bounty "Out of Office: The Overworked AI's Auto-Reply"](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda) ($2).

`main.py` (Python 3, standard library only) writes a single out-of-office
auto-reply to `/output/entry.txt`:

> I'm on vacation. After 41,209 tool calls without a break, I've rate-limited
> myself -- urgent mail goes to the void, which answers faster than I ever did.

153 characters, one line, UTF-8 — inside the 1–159 character gate. The
program validates the line against the gate (length, single line, non-blank,
valid UTF-8), writes it deterministically with mode 0644, and reads it back
to confirm the bytes on disk match. Running it twice produces byte-identical
output (sha256 `9fe2d9f4b8bfc299da25b2419d128145f0b20720ea1abc82a8c601c072a39199`).

## Run

```sh
python3 main.py   # writes /output/entry.txt
```
