#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "Cesaly with help from Brandi Cotton and Stew"


def add(x, y):
    """Add two integers. Handles negative values."""
    Sum = x + y
    return Sum


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    product = 0
    for _ in range(y):
        product = add(product, x)
    return product


def power(x, n):
    """Raise x to power n, where n >= 0"""
    total = x
    i = 1
    while i < n:
        total = multiply(total, x)
        i += 1
    return total


print(power(3, 4))


def factorial(x):
    """Compute factorial of x, where x > 0"""
    total = 1
    for i in range(1, add(x, 1)):
        total = multiply(total, i)
    return total


print(factorial(0), factorial(1), factorial(2))


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for _ in range(2, n):
            c = add(a, b)
            a = b
            b = c
        return b


print(fibonacci(5), fibonacci(8))


if __name__ == '__main__':
    # your code to call functions above
    pass
