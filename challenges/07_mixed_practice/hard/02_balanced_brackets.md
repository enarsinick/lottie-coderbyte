# is_balanced

Return `True` if all the brackets in `s` are balanced and properly nested,
and `False` otherwise.

You're checking three kinds of brackets: `( )`, `[ ]`, `{ }`. Any other
character in the string is ignored — only the brackets matter.

A string is balanced when every opener has a matching closer of the same
type, and the closers happen in the **reverse order** of the openers.

## Examples
| Call | Result | Why |
| --- | --- | --- |
| `is_balanced("()")` | `True` | one pair |
| `is_balanced("()[]{}")` | `True` | three pairs side-by-side |
| `is_balanced("{[]}")` | `True` | properly nested |
| `is_balanced("([)]")` | `False` | wrong nesting order |
| `is_balanced("(]")` | `False` | wrong matching closer |
| `is_balanced("(")` | `False` | unclosed opener |
| `is_balanced(")")` | `False` | closer with nothing to match |
| `is_balanced("(a + [b - c] * {d / e})")` | `True` | non-bracket chars ignored |
| `is_balanced("hello (world)")` | `True` | non-bracket chars ignored |
| `is_balanced("")` | `True` | nothing to be unbalanced |

> 🧠 **Combines:** strings + lists (as a *stack*) + loops + conditionals.
> This is your first taste of a classic data-structure technique: **the stack**.

## Concepts exercised
- iterating over a string
- using a list as a **stack** (`.append` to push, `.pop()` to pop)
- mapping closers to their matching openers using a dict
- early exit when you find a mismatch
- final state check (the stack should be empty at the end)

## Hints

<details><summary>Hint 1 — the idea</summary>

Walk through the string. Use a list as a "stack" — every time you see an
opener (`(`, `[`, `{`), push it onto the stack. Every time you see a closer,
the top of the stack must be the matching opener; otherwise the string is
unbalanced.

At the very end, if the stack is empty, all openers got matched. If anything
is left on the stack, you had unclosed openers.
</details>

<details><summary>Hint 2 — concrete moves</summary>

- A list works as a stack: `stack.append(x)` pushes, `stack.pop()` removes
  and returns the last item, and `stack[-1]` peeks at the top.
- A small dict makes "what's the matching opener for this closer?" easy:
  `pairs = {")": "(", "]": "[", "}": "{"}`.
- Things that should make you return `False` immediately:
  - a closer when the stack is empty (no opener to match)
  - a closer whose match doesn't equal `stack.pop()`
- After the loop, return `len(stack) == 0`.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
pairs = {")": "(", "]": "[", "}": "{"}
make an empty list called stack
for each character ch in s:
    if ch is one of "([{":
        push ch onto stack
    else if ch is one of ")]}":
        if stack is empty:
            return False
        if stack.pop() is not equal to pairs[ch]:
            return False
    # any other character: ignore
return whether stack is empty
```

In Python:

```python
pairs = {")": "(", "]": "[", "}": "{"}
stack = []
for ch in s:
    if ch in "([{":
        stack.append(ch)
    elif ch in ")]}":
        if not stack or stack.pop() != pairs[ch]:
            return False
return len(stack) == 0
```
</details>
