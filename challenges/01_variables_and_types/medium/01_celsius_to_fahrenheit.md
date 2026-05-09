# to_fahrenheit

Convert a temperature from Celsius to Fahrenheit and return the result as a
**float**.

The formula is:

```
F = C * 9/5 + 32
```

## Examples
| Call | Result |
| --- | --- |
| `to_fahrenheit(0)` | `32.0` |
| `to_fahrenheit(100)` | `212.0` |
| `to_fahrenheit(-40)` | `-40.0` |
| `to_fahrenheit(37)` | `98.6` |
| `to_fahrenheit(20)` | `68.0` |

## Concepts exercised
- arithmetic with mixed `int` and `float` values
- the difference between `/` (true division → float) and `//` (floor division → int)
- order of operations

## Hints

<details><summary>Hint 1 — getting started</summary>

Translate the formula straight into Python and return the result. The hardest
part is making sure you get a float, not an int.
</details>

<details><summary>Hint 2 — getting a float result</summary>

In Python, `9/5` is `1.8` (a float, because `/` always returns a float — even
when both sides are ints). So `c * 9/5 + 32` will give you a float
automatically — you don't need to call `float()` yourself.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
return c times 9/5 plus 32
```

That literally is the formula. Operator precedence handles the rest:
multiplication and division happen before addition, so `c * 9/5 + 32` evaluates
as `(c * 9/5) + 32`.
</details>
