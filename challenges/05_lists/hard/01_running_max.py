"""
running_max  —  see 01_running_max.md for the full description.

Given a list of numbers, return a new list of the same length where each
element is the maximum value seen in the input from the start up to (and
including) that position.

If the input list is empty, return an empty list.
"""


def running_max(nums):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    (([3, 1, 4, 1, 5, 9, 2, 6],), [3, 3, 4, 4, 5, 9, 9, 9]),
    (([5, 4, 3, 2, 1],), [5, 5, 5, 5, 5]),
    (([1, 2, 3, 4, 5],), [1, 2, 3, 4, 5]),
    (([7],), [7]),
    (([],), []),
    (([2, 2, 2],), [2, 2, 2]),
    (([-3, -1, -2, -1],), [-3, -1, -1, -1]),
    (([0, 0, 0],), [0, 0, 0]),
]

if __name__ == "__main__":
    name = "running_max"
    fn = running_max
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
