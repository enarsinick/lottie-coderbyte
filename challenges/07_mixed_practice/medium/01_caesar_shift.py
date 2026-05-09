"""
caesar  —  see 01_caesar_shift.md for the full description.

Apply a Caesar cipher to text: shift each letter forward by k positions in the
alphabet, wrapping around from Z back to A. Preserve case (upper stays upper,
lower stays lower). Non-letters (spaces, punctuation, digits) pass through
unchanged.

Combines: strings + conditionals + loops.
"""


def caesar(text, k):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    (("abc", 1), "bcd"),
    (("xyz", 1), "yza"),
    (("Hello, World!", 3), "Khoor, Zruog!"),
    (("ABC", 0), "ABC"),
    (("abc", 26), "abc"),
    (("Z", 1), "A"),
    (("a", 27), "b"),
    (("Python", 13), "Clguba"),
    (("", 5), ""),
    (("123 abc", 2), "123 cde"),
]

if __name__ == "__main__":
    name = "caesar"
    fn = caesar
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
