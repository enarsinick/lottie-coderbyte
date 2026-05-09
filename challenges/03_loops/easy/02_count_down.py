"""
count_down  —  see 02_count_down.md for the full description.

Given a non-negative integer n, return a list counting down from n to 1.
If n is 0, return an empty list.
"""


def count_down(n):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    ((5,), [5, 4, 3, 2, 1]),
    ((1,), [1]),
    ((0,), []),
    ((3,), [3, 2, 1]),
    ((10,), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
    ((2,), [2, 1]),
]

if __name__ == "__main__":
    name = "count_down"
    fn = count_down
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
