from typing import Tuple

from pytest import raises

from fizzbuzz.fizzbuzz import main


def test_fizzbuzz_non_int():
    invalid_entries: Tuple[float, str, list] = ("1", 1.0, [1, 3, 5])

    for invalid_entry in invalid_entries:
        with raises(TypeError):
            main(invalid_entry)


def test_fizzbuzz_input_non_multiplier():
    inputs: Tuple[int] = (-1, 1, 2, 4, 101)

    for input in inputs:
        assert main(input) == str(input)


def test_fizzbuzz_input_multiplier_only_3():
    inputs: Tuple[int] = (3, 6, -3, 18)
    for input in inputs:
        assert main(input) == "Fizz"


def test_fizzbuzz_input_multiplier_only_5():
    inputs: Tuple[int] = (-5, 10, 20, 100)
    for input in inputs:
        assert main(input) == "Buzz"


def test_fizzbuzz_input_multiplier_3_and_5():
    inputs: Tuple[int] = (-15, 0, 15, 45)
    for input in inputs:
        assert main(input) == "Fizzbuzz"
