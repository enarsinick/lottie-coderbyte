"""
count_letters  —  see 01_count_letters.md for the full description.

Given a string, return how many of its characters are alphabetic letters
(A–Z or a–z). Spaces, digits, and punctuation don't count.
"""


def count_letters(s):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    (("Hello",), 5),
    (("Hello, World!",), 10),
    (("",), 0),
    (("123",), 0),
    (("a b c",), 3),
    (("Mr. Frodo",), 7),
    (("   ",), 0),
    (("abc123",), 3),
]

if __name__ == "__main__":
    name = "count_letters"
    fn = count_letters
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
