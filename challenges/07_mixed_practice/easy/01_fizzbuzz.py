"""
fizzbuzz  —  see 01_fizzbuzz.md for the full description.

Return a list of length n where, for each i from 1 to n:
    - if i is divisible by both 3 and 5  ->  "FizzBuzz"
    - else if i is divisible by 3        ->  "Fizz"
    - else if i is divisible by 5        ->  "Buzz"
    - else                                ->  the number i as a string

Combines: loops + conditionals + strings + lists.
"""


def fizzbuzz(n):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    ((1,), ["1"]),
    ((3,), ["1", "2", "Fizz"]),
    ((5,), ["1", "2", "Fizz", "4", "Buzz"]),
    ((6,), ["1", "2", "Fizz", "4", "Buzz", "Fizz"]),
    ((10,), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]),
    (
        (15,),
        [
            "1", "2", "Fizz", "4", "Buzz",
            "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz",
        ],
    ),
    ((0,), []),
]

if __name__ == "__main__":
    name = "fizzbuzz"
    fn = fizzbuzz
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
