"""
    Challenge: Prime number checker
                -- Prime number is a number that can be only divisible by itself and one only.
                -- you may need to use modulus(%).
"""
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0: is_prime = False
    if is_prime: print("It's a prime number.")
    else: print("It's not a prime number.")
n = int(input("Check this number: "))
prime_checker(number = n)