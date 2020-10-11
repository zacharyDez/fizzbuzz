def main(num: int) -> str:
    if type(num) != int:
        raise TypeError("Argument must be an integer.")

    if num % 5 == 0 and num % 3 == 0:
        return "Fizzbuzz"

    if num % 5 == 0:
        return "Buzz"

    if num % 3 == 0:
        return "Fizz"

    return str(num)
