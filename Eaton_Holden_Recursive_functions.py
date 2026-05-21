def factorial(n):
    if n == 0:   
        return 1
    else:
        return n * factorial(n - 1)  
    

def summation(n):
    if n == 1:   
        return 1
    if n == 0:
        return 0
    if n < 0:
        return n + summation(n+1)
    else:
        return n + summation(n - 1)
    
def power(base, exponent):
    if exponent == 0:   
        return 1
    else:
        return base * power(base, exponent - 1)
    

def fibonacci(n):
    if n == 0:   
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def sum_of_numbers_digits(n):
    if n < 1:
        return 0
    number = n % 10
    digit = int(n / 10)
    return sum_of_numbers_digits(digit) + number
    
def multiplication_of_numbers_digits(n):
    if n < 1:
        return 1
    number = n % 10
    digit = int(n / 10)
    return number * multiplication_of_numbers_digits(digit)
    
def product_of_two_whole_numbers(a, b):
    if b == 0:   
        return 0
    return a + product_of_two_whole_numbers(a, b - 1)

def reverse_a_digit_in_a_number(n):
    n = str(n)

    if n == '':
        return n
    return int(n[-1] + str(reverse_a_digit_in_a_number(n[:-1])))

def main():
    print(factorial(5))
    print(summation(-5))
    print(power(-2,4))
    print(fibonacci(10))
    print(sum_of_numbers_digits(6789))
    print(multiplication_of_numbers_digits(232))
    print(product_of_two_whole_numbers(3,5))
    print(reverse_a_digit_in_a_number(456))
main()