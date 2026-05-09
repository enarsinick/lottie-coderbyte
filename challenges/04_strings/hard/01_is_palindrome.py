"""
is_palindrome  —  see 01_is_palindrome.md for the full description.

Return True if the given string reads the same forwards and backwards,
ignoring case differences and any spaces. Other characters (punctuation, etc.)
DO count.
"""


def is_palindrome(s):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    (("racecar",), True),
    (("RaceCar",), True),
    (("hello",), False),
    (("",), True),
    (("a",), True),
    (("ab",), False),
    (("A man a plan a canal Panama",), True),
    (("Was it a car or a cat I saw",), True),
    (("python",), False),
    (("noon",), True),
    (("Hello olleH",), True),
]

if __name__ == "__main__":
    name = "is_palindrome"
    fn = is_palindrome
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
