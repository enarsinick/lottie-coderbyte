# is_palindrome

Return `True` if a string reads the same forwards and backwards, **ignoring
case differences and any spaces**. Return `False` otherwise.

An empty string and a single character should both count as palindromes.

> Note: in this challenge we ignore *spaces and case* but **not** other
> punctuation. The tests don't use any punctuation that would trip you up,
> so you don't need a fancy "strip everything non-alphabetic" step.

## Examples
| Call | Result |
| --- | --- |
| `is_palindrome("racecar")` | `True` |
| `is_palindrome("RaceCar")` | `True` |
| `is_palindrome("noon")` | `True` |
| `is_palindrome("hello")` | `False` |
| `is_palindrome("A man a plan a canal Panama")` | `True` |
| `is_palindrome("Was it a car or a cat I saw")` | `True` |
| `is_palindrome("")` | `True` |
| `is_palindrome("a")` | `True` |
| `is_palindrome("Hello olleH")` | `True` |

## Concepts exercised
- string slicing (and the reverse-slice trick `s[::-1]`)
- string methods (`.lower()`, `.replace()`)
- normalising data before comparing

## Hints

<details><summary>Hint 1 — getting started</summary>

The trick is to *first* normalise the string — strip spaces and convert to
lowercase — and *then* check if the result equals its reverse.
</details>

<details><summary>Hint 2 — Python tools you'll want</summary>

- `s.lower()` returns a new string with all letters lowercased.
- `s.replace(" ", "")` returns a new string with every space removed.
- `s[::-1]` is a slice that reverses a string. (The third number in a slice
  is the step; `-1` means "step backwards by 1".)

Once you've got a clean lowercase, space-free version of the string,
comparing it to `cleaned[::-1]` with `==` gives you the answer.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
cleaned = s with all spaces removed, then lowercased
return cleaned equals cleaned reversed
```

In Python:

```python
cleaned = s.replace(" ", "").lower()
return cleaned == cleaned[::-1]
```

For an empty string, `cleaned` is `""`, and `"" == ""[::-1]` is `True`. For a
single character, the reversed version is the same single character — also
`True`. Both edge cases fall out for free.
</details>
