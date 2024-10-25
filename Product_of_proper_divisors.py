def get_valid_input():
    while True:
        try:
            n = int(input("Enter an integer: "))
            if n >= 0:
                return n
            else:
                return abs(n)
        except ValueError:
            print("Invalid input. Please enter a valid integer: ")


def get_list_of_proper_divisors(n):
    divisor_list = []  # We declare a void list 
    for i in range(2, n // 2 + 1):
        if n % i == 0:  # We check for proper divisors in the smallest range possible
            divisor_list.append(i)  # We add them as elements in the list
            divisor_list.append(-i)  # If a positive number is the divisor of a number than so is it's opposite
    return divisor_list


def test_list():
    assert get_list_of_proper_divisors(6) == [2, -2, 3, -3]
    assert get_list_of_proper_divisors(0) == []
    assert get_list_of_proper_divisors(10) == [2, -2, 5, -5]
    assert get_list_of_proper_divisors(5) == []


def multiply_numbers_in_list(list_of_proper_divisors):
    product_of_divisors = 1  # We initiate the product of divisors with 1 since 1 is the neutral element
    for divisor in list_of_proper_divisors:
        product_of_divisors *= divisor  # We multiply each divisor in the list together
    if list_of_proper_divisors == []:  # In the case the number has no divisors the list will remain empty
        return None
    else:
        return product_of_divisors


def test_multiplication():
    assert multiply_numbers_in_list([2, -2, 3, -3]) == 36
    assert multiply_numbers_in_list([0, 1, 3]) == 0
    assert multiply_numbers_in_list([10, 5, 2]) == 100
    assert multiply_numbers_in_list([0]) == 0
    assert multiply_numbers_in_list([-3, 10]) == 30


def main():
    n = get_valid_input()
    list_of_divisors = get_list_of_proper_divisors(n)
    product_of_divisors = multiply_numbers_in_list(list_of_divisors)
    print("The proper divisors of the number", n, "are: ", list_of_divisors, "\nAnd their product is: ", product_of_divisors)
    test_list()
    test_multiplication()


main()
