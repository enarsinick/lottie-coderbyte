# count_vowels

Given a string `s`, return the number of vowels it contains. A vowel is one of
`a`, `e`, `i`, `o`, or `u` — and the count should be case-insensitive (so `A`
counts the same as `a`). The letter `y` does **not** count as a vowel here.

## Examples
| Call | Result |
| --- | --- |
| `count_vowels("hello")` | `2` |
| `count_vowels("HELLO")` | `2` |
| `count_vowels("aeiou")` | `5` |
| `count_vowels("Bilbo Baggins")` | `4` |
| `count_vowels("Hello, World!")` | `3` |
| `count_vowels("xyz")` | `0` |
| `count_vowels("")` | `0` |

## Concepts exercised
- iterating over a string
- using **`in`** to check membership
- combining a loop, a conditional, and an accumulator
- normalising case before comparing

## Hints

<details><summary>Hint 1 — getting started</summary>

Walk through the string one character at a time. For each character, check
whether it's a vowel and, if so, bump a counter.
</details>

<details><summary>Hint 2 — case-insensitive check with `in`</summary>

The cleanest way to check membership is the `in` operator:

```python
if ch in "aeiou":
    ...
```

To make it case-insensitive, lowercase the character first (`ch.lower()`)
or lowercase the whole string up front (`s = s.lower()`).
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
set count to 0
for each character ch in s:
    if ch.lower() is in "aeiou":
        add 1 to count
return count
```

`y` isn't in `"aeiou"`, so it's automatically excluded. An empty string makes
the loop run zero times, giving `0`.
</details>
