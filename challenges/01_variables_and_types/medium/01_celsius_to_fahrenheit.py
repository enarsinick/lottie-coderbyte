"""
to_fahrenheit  —  see 01_celsius_to_fahrenheit.md for the full description.

Convert a temperature from degrees Celsius to degrees Fahrenheit.
Formula:  F = C * 9/5 + 32
"""


def to_fahrenheit(c):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    ((0,), 32.0),
    ((100,), 212.0),
    ((-40,), -40.0),
    ((37,), 98.6),
    ((20,), 68.0),
    ((25,), 77.0),
]

if __name__ == "__main__":
    name = "to_fahrenheit"
    fn = to_fahrenheit
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
