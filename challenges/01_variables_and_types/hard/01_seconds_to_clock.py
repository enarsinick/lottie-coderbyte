"""
format_time  —  see 01_seconds_to_clock.md for the full description.

Given a number of seconds, return a string formatted as "HH:MM:SS"
with each piece zero-padded to two digits.
"""


def format_time(secs):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    ((0,), "00:00:00"),
    ((59,), "00:00:59"),
    ((60,), "00:01:00"),
    ((61,), "00:01:01"),
    ((3599,), "00:59:59"),
    ((3600,), "01:00:00"),
    ((3661,), "01:01:01"),
    ((86399,), "23:59:59"),
]

if __name__ == "__main__":
    name = "format_time"
    fn = format_time
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
