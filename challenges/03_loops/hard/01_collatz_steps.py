"""
collatz_steps  —  see 01_collatz_steps.md for the full description.

Starting from a positive integer n, repeatedly apply:
    if n is even:  n = n / 2
    if n is odd:   n = 3 * n + 1
…until n equals 1. Return the number of steps it took.
"""


def collatz_steps(n):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    ((1,), 0),
    ((2,), 1),
    ((4,), 2),
    ((3,), 7),
    ((6,), 8),
    ((7,), 16),
    ((8,), 3),
    ((27,), 111),
]

if __name__ == "__main__":
    name = "collatz_steps"
    fn = collatz_steps
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
