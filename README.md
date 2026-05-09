# lottie-coderbyte

A self-paced collection of beginner Python coding challenges. Each challenge is a
single function you fill in. Run the file — instant pass/fail feedback.

## Quick start

Pick any challenge and run it:

```bash
python3 challenges/03_loops/easy/01_sum_to_n.py
```

You'll see one line per test case (PASS or FAIL) and a summary at the bottom.
Open the file, fill in the function body, save, run again. Repeat until everything
is PASS.

## How a challenge is structured

Every challenge is a pair of files:

- `NN_name.py` — the function you write, with the test cases at the bottom of
  the file. **Only edit the function body.** Everything below
  `# === Tests (don't edit below) ===` runs the tests for you.
- `NN_name.md` — the full description, examples, and three progressive hints
  (click to reveal). The deepest hint is a pseudo-code walkthrough — the
  *approach*, not the answer. You still write the Python yourself.

There are no reference solutions in this repo on purpose. If you're truly stuck,
the third hint will get you across the line.

## Folder layout

```
challenges/
  01_variables_and_types/
    easy/        # warm-ups
    medium/      # one step up
    hard/        # combines a few ideas
  02_conditionals/
  03_loops/
  04_strings/
  05_lists/
  06_dictionaries/
  07_mixed_practice/   # combines concepts from earlier topics
```

Recommended path: top-to-bottom, easy-to-hard. Medium and hard challenges in
each topic deliberately reach for ideas from earlier topics, so going in order
keeps things smooth.

## Overall progress

To see how you're doing across every challenge:

```bash
python3 progress.py
```

This runs every challenge file and prints a per-topic and grand-total summary.

## Adding new challenges

Copy `_template/NN_name.py` and `_template/NN_name.md` into the appropriate
`challenges/<topic>/<difficulty>/` folder, rename them, and fill in the
function name, description, examples, hints, and `TESTS` list.

## Requirements

Python 3.10+. No third-party packages — pure standard library.
