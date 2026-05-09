"""
double_each  —  see 02_double_each.md for the full description.

Given a list of numbers, return a new list where each number is doubled.
The original list should not be modified.
"""


def double_each(nums):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    (([1, 2, 3],), [2, 4, 6]),
    (([],), []),
    (([0],), [0]),
    (([-1, -2, -3],), [-2, -4, -6]),
    (([5],), [10]),
    (([1, 1, 1, 1],), [2, 2, 2, 2]),
    (([10, 20, 30, 40],), [20, 40, 60, 80]),
]

if __name__ == "__main__":
    name = "double_each"
    fn = double_each
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
