# count_letters

Given a string `s`, return the number of characters in it that are alphabetic
letters (A–Z or a–z). Spaces, digits, punctuation, and any other non-letter
character don't count.

## Examples
| Call | Result |
| --- | --- |
| `count_letters("Hello")` | `5` |
| `count_letters("Hello, World!")` | `10` |
| `count_letters("Mr. Frodo")` | `7` |
| `count_letters("a b c")` | `3` |
| `count_letters("123")` | `0` |
| `count_letters("")` | `0` |

## Concepts exercised
- iterating over a string character-by-character
- the **accumulator pattern** (counting things in a loop)
- the `.isalpha()` string method

## Hints

<details><summary>Hint 1 — getting started</summary>

You can iterate over a string with `for ch in s:` — each `ch` is a single
character (a one-character string). Keep a counter and bump it whenever
the character is a letter.
</details>

<details><summary>Hint 2 — checking if a character is a letter</summary>

Python strings have a method `.isalpha()` that returns `True` if every
character in the string is alphabetic. Since `ch` is a single character,
`ch.isalpha()` tells you whether that one character is a letter.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
set count to 0
for each character ch in s:
    if ch.isalpha():
        add 1 to count
return count
```

For an empty string the loop never runs, so `count` stays `0` — exactly the
expected answer.
</details>
