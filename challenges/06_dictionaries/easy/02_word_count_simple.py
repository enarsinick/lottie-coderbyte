"""
word_count  —  see 02_word_count_simple.md for the full description.

Given a list of words, return a dictionary mapping each unique word to the
number of times it appears in the list.
"""


def word_count(words):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    ((["a", "b", "a", "c", "a"],), {"a": 3, "b": 1, "c": 1}),
    (([],), {}),
    ((["hello"],), {"hello": 1}),
    ((["one", "two", "two", "three", "three", "three"],), {"one": 1, "two": 2, "three": 3}),
    ((["x", "x", "x"],), {"x": 3}),
    ((["apple", "banana", "apple"],), {"apple": 2, "banana": 1}),
]

if __name__ == "__main__":
    name = "word_count"
    fn = word_count
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
