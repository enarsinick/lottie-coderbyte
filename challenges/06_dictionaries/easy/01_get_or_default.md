# get_or_default

Given a dictionary `d` and a `key`, return the value stored under that key.
If the key isn't in the dictionary, return the string `"missing"` instead.

> Take care: the value `0`, `False`, and `""` are all valid stored values
> and should be returned as-is — only a *missing* key gets `"missing"`.

## Examples
| Call | Result |
| --- | --- |
| `get_or_default({"a": 1, "b": 2}, "a")` | `1` |
| `get_or_default({"a": 1, "b": 2}, "z")` | `"missing"` |
| `get_or_default({}, "x")` | `"missing"` |
| `get_or_default({"name": "Bilbo"}, "age")` | `"missing"` |
| `get_or_default({"x": 0}, "x")` | `0` |
| `get_or_default({"flag": False}, "flag")` | `False` |

## Concepts exercised
- accessing dictionary values
- checking key membership with `in`
- (or, alternatively, the `dict.get()` method)

## Hints

<details><summary>Hint 1 — getting started</summary>

There are two common ways: you can check whether the key is in the dictionary
first with `if key in d`, or you can use a built-in dict method that does
exactly this kind of "get or default" lookup in one step.
</details>

<details><summary>Hint 2 — `in` and `.get()`</summary>

**With `in`:**

```python
if key in d:
    return d[key]
return "missing"
```

**With `.get()`:**

```python
return d.get(key, "missing")
```

`d.get(key, default)` returns `d[key]` if the key exists, otherwise the
default — without raising an error.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
return d.get(key, default="missing")
```

That's a one-liner: `return d.get(key, "missing")`. The `.get()` approach is
the idiomatic Python way and handles every test case (including ones where
the value is `0`, `False`, or `""`) correctly.
</details>
