"""
filter_evens  —  see 01_filter_evens.md for the full description.

Given a list of integers, return a new list containing only the even numbers,
in the same order they appeared in the input.
"""


def filter_evens(nums):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    (([1, 2, 3, 4, 5, 6],), [2, 4, 6]),
    (([1, 3, 5],), []),
    (([2, 4, 6],), [2, 4, 6]),
    (([],), []),
    (([0],), [0]),
    (([-2, -1, 0, 1, 2],), [-2, 0, 2]),
    (([10, 11, 12, 13, 14],), [10, 12, 14]),
    (([7],), []),
]

if __name__ == "__main__":
    name = "filter_evens"
    fn = filter_evens
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
