"""
max_of_two  —  see 02_max_of_two.md for the full description, examples, and hints.

Given two numbers a and b, return the larger one.
If they are equal, return either (the tests use the same value for that case).
"""


def max_of_two(a, b):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    ((3, 5), 5),
    ((10, 2), 10),
    ((7, 7), 7),
    ((-1, -5), -1),
    ((0, 100), 100),
    ((-10, 0), 0),
    ((42, 41), 42),
]

if __name__ == "__main__":
    name = "max_of_two"
    fn = max_of_two
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
