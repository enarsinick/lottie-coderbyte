# inventory_total

Given a `prices` dictionary mapping each item name to its price, and an
`items` list of the items that were bought (with possible duplicates),
return the total cost.

You can assume every item in `items` has an entry in `prices`.

> 🧠 **Combines:** dicts + lists + loops + the accumulator pattern.

## Examples
| Call | Result |
| --- | --- |
| `inventory_total({"apple": 1, "bread": 3, "milk": 2}, ["apple", "bread", "milk"])` | `6` |
| `inventory_total({"apple": 1}, ["apple", "apple", "apple"])` | `3` |
| `inventory_total({"x": 10, "y": 20}, ["x", "y", "x"])` | `40` |
| `inventory_total({"a": 1, "b": 2}, [])` | `0` |
| `inventory_total({"coffee": 4, "muffin": 3, "juice": 2}, ["coffee", "coffee", "muffin", "juice"])` | `13` |

## Concepts exercised
- looking up dictionary values by key
- looping over a list
- the accumulator pattern (a running total)

## Hints

<details><summary>Hint 1 — getting started</summary>

Keep a running total. Walk through the `items` list, look up the price of
each item in `prices`, and add it to the total.
</details>

<details><summary>Hint 2 — the lookup</summary>

Inside the loop, `prices[item]` gives the price of the current item. Add it
to your running total:

```python
total += prices[item]
```
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
set total to 0
for each item in items:
    add prices[item] to total
return total
```

In Python:

```python
total = 0
for item in items:
    total += prices[item]
return total
```

For an empty `items` list the loop runs zero times and you return `0`.
</details>
