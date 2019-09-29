import math

def factorial(n):
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result