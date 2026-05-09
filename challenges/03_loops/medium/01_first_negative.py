"""
first_negative  —  see 01_first_negative.md for the full description.

Given a list of numbers, return the first negative number in the list.
If the list contains no negative numbers (or is empty), return None.
"""


def first_negative(nums):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    (([1, 2, -3, 4, -5],), -3),
    (([1, 2, 3],), None),
    (([],), None),
    (([-1],), -1),
    (([0, 0, 0, -7],), -7),
    (([5, 4, 3, 2, 1],), None),
    (([10, -2, -3],), -2),
    (([0],), None),
]

if __name__ == "__main__":
    name = "first_negative"
    fn = first_negative
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
