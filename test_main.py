from main import greet, add_numbers


def test_greet():
    assert greet("Khalid") == "Hello, Khalid!"


def test_add_numbers():
    assert add_numbers(10, 20) == 30
