#!/usr/bin/env python3
"""
Create a measure_time function with integers n and
max_delay as arguments that measures the total execution
time for wait_n(n, max_delay), and returns total_time / n.
Your function should return a float.
"""

from time import time
from asyncio import run
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n
    (n, max_delay), and return total_time / n.

    Args:
    n (int): Number of coroutines to create.
    max_delay (int): Maximum delay for wait_random.

    Returns:
    float: Average time per coroutine.
    """
    start_time = time()
    run(wait_n(n, max_delay))
    end_time = time()
    total_time = end_time - start_time
    return total_time / n
