"""
first_and_last  —  see 01_first_and_last.md for the full description.

Given a non-empty list, return a new list of length 2 containing the first
and the last element.
"""


def first_and_last(items):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    (([1, 2, 3, 4, 5],), [1, 5]),
    (([1],), [1, 1]),
    (([10, 20],), [10, 20]),
    (([7, 7, 7],), [7, 7]),
    ((["a", "b", "c"],), ["a", "c"]),
    (([0, 0, 0, 99],), [0, 99]),
]

if __name__ == "__main__":
    name = "first_and_last"
    fn = first_and_last
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
