"""
initials  —  see 02_initials.md for the full description.

Given a person's full name as a string, return their initials in uppercase.
The name has one or more parts separated by single spaces.

Combines: strings + loops + lists.
"""


def initials(name):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    (("Bilbo Baggins",), "BB"),
    (("Frodo Baggins",), "FB"),
    (("Albert Einstein",), "AE"),
    (("john doe",), "JD"),
    (("Madonna",), "M"),
    (("Mary Jane Watson",), "MJW"),
    (("a b c d",), "ABCD"),
    (("Guido van Rossum",), "GVR"),
]

if __name__ == "__main__":
    name = "initials"
    fn = initials
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
