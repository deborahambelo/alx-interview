#!/usr/bin/python3
"""
Method to find number of minimum operations to complete a task.
"""


def minOperations(n):
    """
    Only operations are copy and paste.
    Find the smallest number of operations needed to complete the task.
    n = number of times to print the letter H.
    if n is not possible, return 0
    """
    minOps = 0
    div = 2
    while (isinstance(n, int) and n > 1):
        while (n % div):
            div += 1
        minOps += div
        n = n // div
    return minOps
