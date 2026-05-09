# word_count

Given a list of words, return a dictionary mapping each unique word to the
number of times it appears in the list.

## Examples
| Call | Result |
| --- | --- |
| `word_count(["a", "b", "a", "c", "a"])` | `{"a": 3, "b": 1, "c": 1}` |
| `word_count(["hello"])` | `{"hello": 1}` |
| `word_count([])` | `{}` |
| `word_count(["one", "two", "two", "three", "three", "three"])` | `{"one": 1, "two": 2, "three": 3}` |
| `word_count(["apple", "banana", "apple"])` | `{"apple": 2, "banana": 1}` |

## Concepts exercised
- building a dictionary inside a loop
- handling the "key not yet seen" case
- the `dict.get()` method (or an `if key in d` check)

## Hints

<details><summary>Hint 1 — getting started</summary>

Start with an empty dictionary. Walk through the words, and for each word:
- if you've seen it before, add 1 to its count
- if not, set its count to 1
</details>

<details><summary>Hint 2 — three ways to do it</summary>

**With `if word in counts`:**

```python
if word in counts:
    counts[word] += 1
else:
    counts[word] = 1
```

**With `.get()` and a default of `0`:**

```python
counts[word] = counts.get(word, 0) + 1
```

If `word` isn't in `counts` yet, `.get(word, 0)` returns `0`, so the new
count becomes `1`.

**With `collections.Counter`:** the most concise. Look it up if you're
curious — but the two approaches above are great practice in their own right.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
make an empty dictionary called counts
for each word in words:
    counts[word] = counts.get(word, 0) + 1
return counts
```

For an empty list the loop never runs, so you return `{}` — exactly the
expected answer.
</details>
