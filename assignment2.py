def is_odd(num):
    return num % 2 != 0

def sum_of_odd_digits(number):
    odd_sum = 0
    while number > 0:
        digit = number % 10
        if is_odd(digit):
            odd_sum += digit
        number //= 10
    return odd_sum

def sum_of_even_digits(number):
    even_sum = 0
    while number > 0:
        digit = number % 10
        if not is_odd(digit):
            even_sum += digit
        number //= 10
    return even_sum

def difference_of_odd_even_sums(number):
    odd_sum = sum_of_odd_digits(number)
    even_sum = sum_of_even_digits(number)
    return abs(odd_sum - even_sum)
