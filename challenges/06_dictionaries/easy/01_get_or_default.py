"""
get_or_default  —  see 01_get_or_default.md for the full description.

Given a dictionary d and a key, return the value for that key.
If the key is not in the dictionary, return the string "missing" instead.
"""


def get_or_default(d, key):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    (({"a": 1, "b": 2}, "a"), 1),
    (({"a": 1, "b": 2}, "z"), "missing"),
    (({}, "x"), "missing"),
    (({"hello": "world"}, "hello"), "world"),
    (({"name": "Bilbo"}, "age"), "missing"),
    (({"x": 0}, "x"), 0),
    (({"flag": False}, "flag"), False),
]

if __name__ == "__main__":
    name = "get_or_default"
    fn = get_or_default
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
