"""
top_word  —  see 01_top_word.md for the full description.

Given a sentence (a string of words separated by spaces), return the word that
appears the most times. The comparison is case-insensitive: "Hello" and
"HELLO" count as the same word, and the returned word is in lowercase.

You can assume there is always a single clear winner (no ties).
"""


def top_word(sentence):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    (("the quick brown fox jumps over the lazy dog the",), "the"),
    (("hello world hello",), "hello"),
    (("python python python java",), "python"),
    (("one fish two fish red fish blue fish",), "fish"),
    (("only",), "only"),
    (("Hello HELLO hello world",), "hello"),
    (("apple banana apple cherry apple",), "apple"),
]

if __name__ == "__main__":
    name = "top_word"
    fn = top_word
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
