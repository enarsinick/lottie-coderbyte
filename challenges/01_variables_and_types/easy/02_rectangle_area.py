"""
area  —  see 02_rectangle_area.md for the full description, examples, and hints.

Given the width and height of a rectangle, return its area.
"""


def area(width, height):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    ((3, 4), 12),
    ((5, 5), 25),
    ((1, 1), 1),
    ((0, 10), 0),
    ((10, 7), 70),
    ((12, 8), 96),
]

if __name__ == "__main__":
    name = "area"
    fn = area
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
