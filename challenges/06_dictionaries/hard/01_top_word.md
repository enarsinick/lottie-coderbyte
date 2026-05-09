# top_word

Given a `sentence` — a string of words separated by spaces — return the word
that appears the most times.

The comparison is **case-insensitive**: `"Hello"` and `"HELLO"` count as the
same word, and the word you return should be in lowercase.

You can assume there is always a single clear winner (no ties to worry
about). The input always contains at least one word.

## Examples
| Call | Result |
| --- | --- |
| `top_word("the quick brown fox jumps over the lazy dog the")` | `"the"` |
| `top_word("hello world hello")` | `"hello"` |
| `top_word("one fish two fish red fish blue fish")` | `"fish"` |
| `top_word("only")` | `"only"` |
| `top_word("Hello HELLO hello world")` | `"hello"` |

## Concepts exercised
- splitting a string into words with `.split()`
- normalising case before comparison (`.lower()`)
- counting items into a dictionary
- finding the dictionary entry with the largest value

## Hints

<details><summary>Hint 1 — getting started</summary>

Three steps:
1. Split the sentence into a list of words.
2. Count how many times each word appears (case-insensitive).
3. Find the word with the highest count.
</details>

<details><summary>Hint 2 — the building blocks</summary>

- `sentence.lower().split()` gives you a lowercase list of words. (`.split()`
  with no argument splits on whitespace, which is exactly what we want.)
- To count, build a dict: `counts[word] = counts.get(word, 0) + 1`.
- To find the entry with the largest value, you can loop over `counts.items()`
  and keep track of the best so far — or use `max(counts, key=counts.get)`,
  which finds the *key* whose *value* is the largest.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
words = sentence lowercased then split on whitespace
counts = empty dict
for each word in words:
    counts[word] = counts.get(word, 0) + 1

set best_word to None and best_count to -1
for each (word, count) in counts.items():
    if count is greater than best_count:
        set best_word to word
        set best_count to count
return best_word
```

If you'd like the shortest version once your loop version works:

```python
words = sentence.lower().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
return max(counts, key=counts.get)
```

`max(counts, key=counts.get)` walks every key in `counts` and picks the one
where `counts[key]` is biggest.
</details>
