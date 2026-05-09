# running_max

Given a list of numbers, return a new list of the same length. Each element
of the result is the **maximum value seen so far** in the input — that is,
the largest of all the numbers from the start of the list up to and including
the current position.

If the input is empty, return an empty list.

## Examples
| Call | Result |
| --- | --- |
| `running_max([3, 1, 4, 1, 5, 9, 2, 6])` | `[3, 3, 4, 4, 5, 9, 9, 9]` |
| `running_max([5, 4, 3, 2, 1])` | `[5, 5, 5, 5, 5]` |
| `running_max([1, 2, 3, 4, 5])` | `[1, 2, 3, 4, 5]` |
| `running_max([7])` | `[7]` |
| `running_max([-3, -1, -2, -1])` | `[-3, -1, -1, -1]` |
| `running_max([])` | `[]` |

Walk through the first one: start at `3`. After seeing `1`, the max so far is
still `3`. After `4`, the max is now `4`. After another `1`, max stays `4`.
After `5`, max is `5`. And so on.

## Concepts exercised
- the **accumulator pattern** (here: tracking a running maximum)
- combining a loop with a conditional
- building a result list as you go
- handling the very first element (which has nothing to compare against)

## Hints

<details><summary>Hint 1 — getting started</summary>

Keep a variable that holds the largest number you've seen so far. As you
walk through the input, compare each new number to it; if the new one is
bigger, update the running max. Either way, append the current running max
to your result list.
</details>

<details><summary>Hint 2 — getting started cleanly</summary>

The first iteration is the tricky part — there's no "previous max" to
compare against. The common trick is to **initialise the running max with
the first element**, then loop from the second element onwards:

```python
if not nums:
    return []
current_max = nums[0]
result = [current_max]
for x in nums[1:]:
    ...
```

`nums[1:]` is a slice — it's all elements from index 1 onward.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
if nums is empty:
    return []
set current_max to the first element
make result equal to [current_max]
for each x in nums starting from the second element:
    if x is greater than current_max:
        set current_max to x
    append current_max to result
return result
```

In Python:

```python
if not nums:
    return []
current_max = nums[0]
result = [current_max]
for x in nums[1:]:
    if x > current_max:
        current_max = x
    result.append(current_max)
return result
```
</details>
