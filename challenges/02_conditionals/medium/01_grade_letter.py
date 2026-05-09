"""
grade  —  see 01_grade_letter.md for the full description, examples, and hints.

Given a numeric score from 0 to 100, return the letter grade:
    90 or above -> "A"
    80 to 89    -> "B"
    70 to 79    -> "C"
    60 to 69    -> "D"
    below 60    -> "F"
"""


def grade(score):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    ((100,), "A"),
    ((95,), "A"),
    ((90,), "A"),
    ((89,), "B"),
    ((85,), "B"),
    ((80,), "B"),
    ((75,), "C"),
    ((70,), "C"),
    ((65,), "D"),
    ((60,), "D"),
    ((59,), "F"),
    ((0,), "F"),
]

if __name__ == "__main__":
    name = "grade"
    fn = grade
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
