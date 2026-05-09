# fizzbuzz

The classic. Given a non-negative integer `n`, return a list of length `n`
where the entry for each number `i` from 1 to `n` is:

- `"FizzBuzz"` if `i` is divisible by **both 3 and 5**
- `"Fizz"`     if `i` is divisible by 3 (but not 5)
- `"Buzz"`     if `i` is divisible by 5 (but not 3)
- the number `i` as a string otherwise

If `n` is `0`, return an empty list.

> 🧠 **Combines:** loops + conditionals + strings + lists.

## Examples
| Call | Result |
| --- | --- |
| `fizzbuzz(5)` | `["1", "2", "Fizz", "4", "Buzz"]` |
| `fizzbuzz(6)` | `["1", "2", "Fizz", "4", "Buzz", "Fizz"]` |
| `fizzbuzz(15)` | `["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]` |
| `fizzbuzz(0)` | `[]` |

## Concepts exercised
- looping over `range`
- `if` / `elif` / `else` chains
- the `%` operator for divisibility
- converting numbers to strings (`str(i)` or an f-string)
- building a list with `.append`

## Hints

<details><summary>Hint 1 — getting started</summary>

Walk from `1` to `n` (inclusive). For each number, decide which of the four
strings (`"FizzBuzz"`, `"Fizz"`, `"Buzz"`, or `str(i)`) to append to your
result list.
</details>

<details><summary>Hint 2 — order of the checks</summary>

The order matters! If you check `i % 3 == 0` first, the number `15` would
match it and you'd append `"Fizz"` — which is wrong, because `15` should be
`"FizzBuzz"`.

Check the most specific case first: divisible by *both* 3 and 5 (i.e.
divisible by 15). Then 3, then 5, then the fallback.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
make an empty list called result
for each i from 1 to n (inclusive):
    if i is divisible by 15:
        append "FizzBuzz" to result
    else if i is divisible by 3:
        append "Fizz" to result
    else if i is divisible by 5:
        append "Buzz" to result
    else:
        append str(i) to result
return result
```

For `n = 0`, `range(1, 1)` is empty so the loop never runs and you return `[]`.
</details>
