"""
is_even  —  see 01_is_even.md for the full description, examples, and hints.

Given an integer, return True if it is even, False otherwise.
"""


def is_even(n):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    ((0,), True),
    ((1,), False),
    ((2,), True),
    ((7,), False),
    ((-4,), True),
    ((-3,), False),
    ((100,), True),
    ((101,), False),
]

if __name__ == "__main__":
    name = "is_even"
    fn = is_even
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
