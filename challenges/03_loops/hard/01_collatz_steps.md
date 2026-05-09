# collatz_steps

Starting from a positive integer `n`, repeatedly apply this rule:

- if `n` is even, replace it with `n / 2`
- if `n` is odd, replace it with `3 * n + 1`

…until `n` becomes `1`. Return the number of steps it took.

If `n` is already `1`, the answer is `0` (zero steps needed).

This is the famous **Collatz conjecture**: it's believed that this process
always reaches `1` for any starting value, though no one has proven it.

## Examples
| Call | Result | Sequence |
| --- | --- | --- |
| `collatz_steps(1)` | `0` | already 1 |
| `collatz_steps(2)` | `1` | 2 → 1 |
| `collatz_steps(4)` | `2` | 4 → 2 → 1 |
| `collatz_steps(3)` | `7` | 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 |
| `collatz_steps(7)` | `16` | 7 → 22 → 11 → 34 → ... → 1 |
| `collatz_steps(27)` | `111` | (a famously long sequence!) |

## Concepts exercised
- `while` loops (loop until a condition is met, not for a fixed count)
- `if` / `else` inside a loop
- updating a variable each iteration
- using **integer division** `//` to keep `n` as an `int`

## Hints

<details><summary>Hint 1 — getting started</summary>

A `while` loop is the right tool: keep going **as long as** `n` is not yet
`1`. Inside the loop, decide whether to halve `n` or apply `3n + 1`, and
remember to count the step.
</details>

<details><summary>Hint 2 — keeping `n` as an integer</summary>

If you write `n = n / 2`, Python gives you a float (e.g. `4 / 2` is `2.0`,
not `2`). That'll mess up the even/odd check on the next iteration.

Use **integer division** `//` instead: `n = n // 2` keeps `n` as an int.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
set steps to 0
while n is not 1:
    if n is even:
        n = n // 2
    else:
        n = 3 * n + 1
    add 1 to steps
return steps
```

When `n` is already `1`, the `while` condition is false on the very first
check, the loop never runs, and `steps` stays `0`. Correct.
</details>
