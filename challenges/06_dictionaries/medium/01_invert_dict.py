"""
invert  —  see 01_invert_dict.md for the full description.

Given a dictionary, return a new dictionary with the keys and values swapped.
You can assume the values are all unique and are themselves valid dict keys
(strings, numbers, etc.).
"""


def invert(d):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    (({"a": 1, "b": 2},), {1: "a", 2: "b"}),
    (({},), {}),
    (({"hello": "world"},), {"world": "hello"}),
    (({"x": 1},), {1: "x"}),
    (({"a": 1, "b": 2, "c": 3},), {1: "a", 2: "b", 3: "c"}),
    (({"name": "Bilbo", "home": "Shire"},), {"Bilbo": "name", "Shire": "home"}),
    (({1: "one", 2: "two"},), {"one": 1, "two": 2}),
]

if __name__ == "__main__":
    name = "invert"
    fn = invert
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
