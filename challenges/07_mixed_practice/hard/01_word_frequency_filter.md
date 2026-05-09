# frequent_words

Given a sentence (a string of words separated by spaces) and a `min_count`,
return a dictionary mapping each word that appears **at least `min_count`
times** in the sentence to the number of times it appears.

The comparison is **case-insensitive**: `"Hello"` and `"HELLO"` count as the
same word, and the keys in the returned dictionary should be lowercase.

> 🧠 **Combines:** strings + dicts + loops + conditionals.

## Examples
| Call | Result |
| --- | --- |
| `frequent_words("the quick brown fox jumps over the lazy dog the", 2)` | `{"the": 3}` |
| `frequent_words("a b a b c", 2)` | `{"a": 2, "b": 2}` |
| `frequent_words("a a a b b c", 2)` | `{"a": 3, "b": 2}` |
| `frequent_words("hello", 1)` | `{"hello": 1}` |
| `frequent_words("a b c", 2)` | `{}` |
| `frequent_words("Hello hello HELLO world", 2)` | `{"hello": 3}` |
| `frequent_words("", 1)` | `{}` |

## Concepts exercised
- splitting a string and lowercasing
- counting items with a dictionary
- iterating a dictionary and **filtering** based on its values
- handling empty input

## Hints

<details><summary>Hint 1 — getting started</summary>

Two phases:

1. **Count** every word, case-insensitively. (This is exactly the
   `word_count` challenge from the dictionaries topic, with a `.lower()` and
   `.split()` step at the start.)
2. **Filter** the counts: build a new dict that only contains the entries
   whose count is at least `min_count`.
</details>

<details><summary>Hint 2 — the building blocks</summary>

- `sentence.lower().split()` gives a lowercase list of words.
- `counts[word] = counts.get(word, 0) + 1` builds the count dict.
- To filter, loop over `counts.items()` and append entries whose count
  meets the threshold:

```python
result = {}
for word, count in counts.items():
    if count >= min_count:
        result[word] = count
```

Or use a dict comprehension once it clicks:
`{w: c for w, c in counts.items() if c >= min_count}`.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
words = sentence lowercased and split on whitespace
counts = empty dict
for each word in words:
    counts[word] = counts.get(word, 0) + 1

result = empty dict
for each (word, count) in counts.items():
    if count is at least min_count:
        result[word] = count
return result
```

For an empty sentence, `"".split()` returns `[]`, so `counts` ends up empty
and `result` is also empty — exactly the expected `{}`.
</details>
