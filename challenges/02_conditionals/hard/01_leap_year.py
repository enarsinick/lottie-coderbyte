"""
is_leap_year  —  see 01_leap_year.md for the full description.

Return True if the given year is a leap year, False otherwise.

A year is a leap year if:
    - it is divisible by 4
    - AND (it is not divisible by 100, OR it is divisible by 400)
"""


def is_leap_year(year):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    ((2000,), True),
    ((2400,), True),
    ((2024,), True),
    ((1996,), True),
    ((4,), True),
    ((1900,), False),
    ((2100,), False),
    ((2023,), False),
    ((1,), False),
    ((2001,), False),
]

if __name__ == "__main__":
    name = "is_leap_year"
    fn = is_leap_year
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
