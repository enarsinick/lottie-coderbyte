# greet

Given a name as a string, return the greeting `"Hello, <name>!"` — that is, the
word `Hello`, a comma and a space, the name itself, and an exclamation mark.

## Examples
| Call | Result |
| --- | --- |
| `greet("World")` | `"Hello, World!"` |
| `greet("Bilbo")` | `"Hello, Bilbo!"` |
| `greet("Mr. Frodo")` | `"Hello, Mr. Frodo!"` |
| `greet("")` | `"Hello, !"` |

## Concepts exercised
- string variables
- string concatenation or f-strings
- returning a value from a function

## Hints

<details><summary>Hint 1 — getting started</summary>

You need to build a new string out of the literal text `"Hello, "`, the
`name` variable, and `"!"`.
</details>

<details><summary>Hint 2 — two ways to do it</summary>

Either use string concatenation with `+`:

```python
"Hello, " + name + "!"
```

…or an f-string:

```python
f"Hello, {name}!"
```

Both are valid. F-strings are usually nicer to read.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
return the string formed by joining "Hello, " then name then "!"
```

There's no edge case to worry about: even an empty name gives `"Hello, !"`,
which is what the tests expect.
</details>
