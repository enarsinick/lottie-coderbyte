"""
inventory_total  —  see 02_inventory_total.md for the full description.

Given a price list (a dict mapping item name -> price) and a list of items
that were bought, return the total cost.

You can assume every item in the bought list has an entry in the prices dict.

Combines: dicts + lists + loops.
"""


def inventory_total(prices, items):
    # Your code here
    pass


# === Tests (don't edit below) ==========================================
TESTS = [
    (({"apple": 1, "bread": 3, "milk": 2}, ["apple", "bread", "milk"]), 6),
    (({"apple": 1}, ["apple", "apple", "apple"]), 3),
    (({"a": 1, "b": 2}, []), 0),
    (({"a": 5}, ["a"]), 5),
    (({"x": 10, "y": 20}, ["x", "y", "x"]), 40),
    (({"a": 0}, ["a", "a", "a"]), 0),
    (({"coffee": 4, "muffin": 3, "juice": 2}, ["coffee", "coffee", "muffin", "juice"]), 13),
]

if __name__ == "__main__":
    name = "inventory_total"
    fn = inventory_total
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
