from task1.solution import strict


@strict
def concat_strings(a: str, b: str) -> str:
    return a + b


@strict
def multiply(a: int, b: int) -> int:
    return a * b


@strict
def is_equal(a: bool, b: bool) -> bool:
    return a == b


@strict
def divide(a: float, b: float) -> float:
    return a / b


def run_tests():
    assert concat_strings("Hello", "World") == "HelloWorld"
    try:
        concat_strings("Hello", 5)
    except TypeError as e:
        assert str(e) == "Аргумент 5 должен быть типа <class 'str'>, а он int"

    assert multiply(2, 3) == 6
    try:
        multiply(2, "3")
    except TypeError as e:
        assert str(e) == "Аргумент 3 должен быть типа <class 'int'>, а он str"

    assert is_equal(True, False) is False
    try:
        is_equal(True, 1)
    except TypeError as e:
        assert str(e) == "Аргумент 1 должен быть типа <class 'bool'>, а он int"

    assert divide(5.0, 2.0) == 2.5
    try:
        divide(5.0, "2.0")
    except TypeError as e:
        assert str(e) == "Аргумент 2.0 должен быть типа <class 'float'>, а он str"

    assert concat_strings(a="Hi", b="There") == "HiThere"
    try:
        concat_strings(a="Hi", b=42)
    except TypeError as e:
        assert str(e) == "Аргумент b должен быть типа <class 'str'>, а он <class 'int'>"

    print("Все тесты пройдены!")


if __name__ == "__main__":
    run_tests()
