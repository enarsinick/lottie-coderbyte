"""
sum_to_n  —  see 01_sum_to_n.md for the full description, examples, and hints.

Return the sum of all integers from 1 to n (inclusive).
Return 0 if n is 0 or negative.
"""


def sum_to_n(n):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    ((1,), 1),
    ((5,), 15),
    ((10,), 55),
    ((100,), 5050),
    ((0,), 0),
    ((-3,), 0),
    ((2,), 3),
]

if __name__ == "__main__":
    name = "sum_to_n"
    fn = sum_to_n
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
