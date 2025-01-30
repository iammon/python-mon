# This program will implement RSA algorithm

# Use to generate random numbers for the prime testing and key generation
import random

def mod_exp(base, exp, mod):
    # Computes the (base^exp) % mod using modular exponentiation
    # This method efficiently calculates large exponentiations under a modulus,
    # which is crucial for cryptographic application like RSA
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //=2
    return result

# Performs Fermat's primality test with k iterations
# This probabilistic test checks if a number is prime by verifying that
# a^(n-1) ≡ 1