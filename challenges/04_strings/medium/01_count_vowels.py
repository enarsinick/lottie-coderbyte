"""
count_vowels  —  see 01_count_vowels.md for the full description.

Given a string, return the number of vowels in it.
A vowel is a, e, i, o, or u — counted whether it's uppercase or lowercase.
"""


def count_vowels(s):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    (("hello",), 2),
    (("HELLO",), 2),
    (("xyz",), 0),
    (("",), 0),
    (("aeiou",), 5),
    (("AEIOU",), 5),
    (("Hello, World!",), 3),
    (("Bilbo Baggins",), 4),
    (("y",), 0),
    (("rhythms",), 0),
]

if __name__ == "__main__":
    name = "count_vowels"
    fn = count_vowels
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
