# shout

Given a string `s`, return it converted to uppercase with an exclamation mark
appended at the end.

## Examples
| Call | Result |
| --- | --- |
| `shout("hello")` | `"HELLO!"` |
| `shout("Python")` | `"PYTHON!"` |
| `shout("WHAT")` | `"WHAT!"` |
| `shout("hi there")` | `"HI THERE!"` |
| `shout("")` | `"!"` |

## Concepts exercised
- string methods (`.upper()`)
- string concatenation with `+`
- (or, alternatively, f-strings)

## Hints

<details><summary>Hint 1 — getting started</summary>

There's a built-in string method that turns a string into all uppercase
letters. Find it, then stick a `"!"` on the end.
</details>

<details><summary>Hint 2 — `.upper()` and concatenation</summary>

`s.upper()` returns a new string with every letter converted to uppercase.
You can join two strings together with `+`:

```python
"HELLO" + "!"   # -> "HELLO!"
```
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
return s.upper() concatenated with "!"
```

In Python: `return s.upper() + "!"`. An f-string also works:
`return f"{s.upper()}!"`.

For an empty string, `s.upper()` is still `""`, so the result is `"!"` —
exactly the expected output.
</details>
