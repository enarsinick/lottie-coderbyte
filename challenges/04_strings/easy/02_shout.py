"""
shout  —  see 02_shout.md for the full description.

Given a string, return it in ALL CAPS with an exclamation mark added at the end.
"""


def shout(s):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    (("hello",), "HELLO!"),
    (("Python",), "PYTHON!"),
    (("WHAT",), "WHAT!"),
    (("",), "!"),
    (("a",), "A!"),
    (("hi there",), "HI THERE!"),
    (("Mixed CASE",), "MIXED CASE!"),
]

if __name__ == "__main__":
    name = "shout"
    fn = shout
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
