# caesar

Apply a **Caesar cipher** to `text`: shift each letter forward by `k`
positions in the alphabet, wrapping around from `Z` back to `A`.

Rules:
- Uppercase letters stay uppercase, lowercase stay lowercase.
- Non-letter characters (spaces, punctuation, digits) pass through unchanged.
- `k` is a non-negative integer. It can be larger than 26 — e.g. `k = 27`
  has the same effect as `k = 1`.

> 🧠 **Combines:** strings + conditionals + loops, with a sprinkle of arithmetic.

## Examples
| Call | Result |
| --- | --- |
| `caesar("abc", 1)` | `"bcd"` |
| `caesar("xyz", 1)` | `"yza"` |
| `caesar("Hello, World!", 3)` | `"Khoor, Zruog!"` |
| `caesar("Z", 1)` | `"A"` |
| `caesar("Python", 13)` | `"Clguba"` (ROT13) |
| `caesar("123 abc", 2)` | `"123 cde"` |
| `caesar("abc", 26)` | `"abc"` (full cycle) |

## Concepts exercised
- looping over a string character by character
- conditionals to handle three cases (uppercase / lowercase / other)
- the `ord()` and `chr()` functions to do letter arithmetic
- `%` to wrap around the alphabet

## Hints

<details><summary>Hint 1 — getting started</summary>

Loop over each character. For each one:
- if it's an uppercase letter, shift it (wrapping from Z to A)
- if it's a lowercase letter, shift it (wrapping from z to a)
- otherwise, leave it alone

Build the result string as you go (or collect the characters in a list and
`"".join(...)` at the end).
</details>

<details><summary>Hint 2 — letter arithmetic with `ord` and `chr`</summary>

`ord("A")` is `65`, `ord("a")` is `97`. `chr(65)` is `"A"`, `chr(97)` is `"a"`.
The 26 lowercase letters are `chr(97)` through `chr(122)`.

To shift a letter: convert it to a 0–25 offset relative to the start of its
alphabet, add `k`, take modulo 26 to wrap, and convert back:

```python
offset = ord(ch) - ord("a")        # 0..25
new_offset = (offset + k) % 26     # still 0..25
new_ch = chr(new_offset + ord("a"))
```

The same recipe works for uppercase using `"A"` instead of `"a"`.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
make an empty string called result
for each character ch in text:
    if ch is uppercase:
        offset = ord(ch) - ord("A")
        new_ch = chr(((offset + k) % 26) + ord("A"))
    else if ch is lowercase:
        offset = ord(ch) - ord("a")
        new_ch = chr(((offset + k) % 26) + ord("a"))
    else:
        new_ch = ch
    append new_ch to result
return result
```

`ch.isupper()` and `ch.islower()` are clean ways to check the case. The `% 26`
takes care of wrap-around (Z → A) automatically, and it also handles `k`
values larger than 26 for free.
</details>
