# initials

Given a person's full name as a string, return their initials in uppercase.
The name has one or more parts separated by single spaces, and you take the
first letter of each part.

> 🧠 **Combines:** strings + loops + lists.

## Examples
| Call | Result |
| --- | --- |
| `initials("Bilbo Baggins")` | `"BB"` |
| `initials("Albert Einstein")` | `"AE"` |
| `initials("john doe")` | `"JD"` |
| `initials("Madonna")` | `"M"` |
| `initials("Mary Jane Watson")` | `"MJW"` |
| `initials("Guido van Rossum")` | `"GVR"` |

## Concepts exercised
- splitting a string with `.split()`
- looping over the resulting list
- string indexing (`part[0]` for the first character)
- uppercasing
- joining strings together

## Hints

<details><summary>Hint 1 — getting started</summary>

Three steps:
1. Split the name into a list of parts.
2. Take the first character of each part.
3. Glue those characters into one uppercase string.
</details>

<details><summary>Hint 2 — the building blocks</summary>

- `name.split()` (no argument) splits on whitespace and gives you a list of
  parts: `"Bilbo Baggins".split()` → `["Bilbo", "Baggins"]`.
- For each `part`, `part[0]` is the first character.
- `.upper()` uppercases a string. You can call it on the final result, or on
  each individual letter.
- You can join strings with `+` in a loop, or use `"".join([...])`.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
make an empty string called result
for each part in name.split():
    add part[0] uppercased to result
return result
```

In Python, with a loop:

```python
result = ""
for part in name.split():
    result += part[0].upper()
return result
```

Or as a one-liner using `.join()`:
`return "".join(part[0].upper() for part in name.split())`.
</details>
