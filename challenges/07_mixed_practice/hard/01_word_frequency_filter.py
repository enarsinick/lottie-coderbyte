"""
frequent_words  —  see 01_word_frequency_filter.md for the full description.

Given a sentence (string of words separated by spaces) and a min_count, return
a dictionary mapping each word that appears at least min_count times to the
number of times it appears.

The comparison is case-insensitive: keys in the result should be lowercase.

Combines: strings + dicts + loops + conditionals.
"""


def frequent_words(sentence, min_count):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    (("the quick brown fox jumps over the lazy dog the", 2), {"the": 3}),
    (("a b a b c", 2), {"a": 2, "b": 2}),
    (("hello", 1), {"hello": 1}),
    (("a b c", 2), {}),
    (("a a a b b c", 2), {"a": 3, "b": 2}),
    (("Hello hello HELLO world", 2), {"hello": 3}),
    (("", 1), {}),
    (("apple banana apple cherry apple banana", 3), {"apple": 3}),
]

if __name__ == "__main__":
    name = "frequent_words"
    fn = frequent_words
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
