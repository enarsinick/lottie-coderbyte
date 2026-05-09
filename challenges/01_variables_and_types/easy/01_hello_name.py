"""
greet  —  see 01_hello_name.md for the full description, examples, and hints.

Given a name, return the greeting "Hello, <name>!".
"""


def greet(name):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    (("World",), "Hello, World!"),
    (("Bilbo",), "Hello, Bilbo!"),
    (("Mr. Frodo",), "Hello, Mr. Frodo!"),
    (("",), "Hello, !"),
    (("python",), "Hello, python!"),
]

if __name__ == "__main__":
    name = "greet"
    fn = greet
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
