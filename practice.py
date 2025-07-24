#Write a function that tells me if a number is prime 
# The function should take an integer and return truie if the integer is prime
# function should throw an error if the input is not a postive inteter


def is_prime(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
