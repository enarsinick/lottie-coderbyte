# invert

Given a dictionary `d`, return a new dictionary where every key/value pair
has been **swapped**: each value in the input becomes a key in the output,
and each key in the input becomes its associated value.

You can assume the values in the input dictionary are all unique and are
themselves valid dict keys (strings, numbers, etc.).

## Examples
| Call | Result |
| --- | --- |
| `invert({"a": 1, "b": 2})` | `{1: "a", 2: "b"}` |
| `invert({"hello": "world"})` | `{"world": "hello"}` |
| `invert({"name": "Bilbo", "home": "Shire"})` | `{"Bilbo": "name", "Shire": "home"}` |
| `invert({})` | `{}` |
| `invert({1: "one", 2: "two"})` | `{"one": 1, "two": 2}` |

## Concepts exercised
- iterating over a dictionary's `.items()`
- building a new dictionary inside a loop
- (or, alternatively, dict comprehensions)

## Hints

<details><summary>Hint 1 — getting started</summary>

You need to walk over every key/value pair of `d` and put them into a new
dictionary in the opposite direction.

`d.items()` gives you `(key, value)` pairs you can loop over.
</details>

<details><summary>Hint 2 — looping over `.items()`</summary>

```python
for k, v in d.items():
    ...
```

Inside the loop, `k` is the key from `d` and `v` is its value. To invert,
you want the *value* to become a key in your new dict, and the *key* to
become the new value: `result[v] = k`.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
make an empty dictionary called result
for each (k, v) in d.items():
    result[v] = k
return result
```

In Python, with a loop:

```python
result = {}
for k, v in d.items():
    result[v] = k
return result
```

Or as a one-liner with a dict comprehension:
`return {v: k for k, v in d.items()}`.
</details>
