# first_and_last

Given a non-empty list, return a new list of length 2 containing the **first**
element and the **last** element of the input.

If the list has only one element, both slots in the result are that element.

## Examples
| Call | Result |
| --- | --- |
| `first_and_last([1, 2, 3, 4, 5])` | `[1, 5]` |
| `first_and_last([1])` | `[1, 1]` |
| `first_and_last([10, 20])` | `[10, 20]` |
| `first_and_last(["a", "b", "c"])` | `["a", "c"]` |
| `first_and_last([0, 0, 0, 99])` | `[0, 99]` |

## Concepts exercised
- list indexing
- **negative indexing** (the `-1` trick)
- building a new list with `[ ... ]`

## Hints

<details><summary>Hint 1 — getting started</summary>

The first element of a list is at index `0`. You also need the last element.
You could use `items[len(items) - 1]` — but Python has a much shorter way.
</details>

<details><summary>Hint 2 — negative indexing</summary>

Python lets you index from the end of a list with negative numbers:
- `items[-1]` is the last element
- `items[-2]` is the second-to-last
- and so on

So `items[0]` and `items[-1]` give you the two values you need.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
return a new list containing items[0] and items[-1]
```

In Python: `return [items[0], items[-1]]`.

For a single-element list, `items[0]` and `items[-1]` are the same element,
so the result is `[x, x]` — exactly what the tests expect.
</details>
