#!/usr/bin/env python3

# lib/sequences.py

def print_fibonacci(length):
    """
    Prints a list of the Fibonacci sequence up to the specified length.

    Args:
    - length (int): The length of the Fibonacci sequence to print.

    Returns:
    - list: The Fibonacci sequence.
    """
    fibonacci_sequence = []  # Initialize an empty list for the sequence

    # Generate the Fibonacci sequence
    a, b = 0, 1
    for _ in range(length):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    print(fibonacci_sequence)  # Print the Fibonacci sequence
    return fibonacci_sequence
