"""
is_balanced  —  see 02_balanced_brackets.md for the full description.

Return True if all the brackets in the string are balanced and properly
nested. The brackets we care about are:  ( )   [ ]   { }
Any other characters in the string should be ignored.

Combines: strings + lists (used as a stack) + loops + conditionals.
"""


def is_balanced(s):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    (("",), True),
    (("()",), True),
    (("()[]{}",), True),
    (("(]",), False),
    (("([)]",), False),
    (("{[]}",), True),
    (("(",), False),
    ((")",), False),
    (("hello (world)",), True),
    (("(a + [b - c] * {d / e})",), True),
    (("((()))",), True),
    (("(()",), False),
    (("({[}])",), False),
    (("no brackets at all",), True),
    (("[",), False),
    (("}",), False),
]

if __name__ == "__main__":
    name = "is_balanced"
    fn = is_balanced
    print(f"\nChallenge: {name}")
    passed = 0
    for args, expected in TESTS:
        args_str = ", ".join(repr(a) for a in args)
        try:
            actual = fn(*args)
            ok = actual == expected
            actual_str = repr(actual)
        except Exception as exc:
            actual_str = f"{type(exc).__name__}: {exc}"
            ok = False
        if ok:
            print(f"  PASS  {name}({args_str}) -> {actual_str}")
        else:
            print(f"  FAIL  {name}({args_str}) expected {expected!r}, got {actual_str}")
        passed += int(ok)
    total = len(TESTS)
    msg = "All passed!" if passed == total and total > 0 else "Keep going!"
    print(f"\n{passed}/{total} tests passed. {msg}")
