from hello import greet, add


def test_greet():
    assert greet("World") == "Hello, World!"
    assert greet("Jas") == "Hello, Jas!"
    assert greet("") == "Hello, !"
    assert greet("Alice & Bob") == "Hello, Alice & Bob!"
    assert greet("A" * 1000) == f"Hello, {'A' * 1000}!"


def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(-3, -4) == -7
    assert add(1.5, 2.5) == 4.0
    assert add(10**9, 10**9) == 2 * 10**9
