#!/usr/bin/env python3
"""
An asynchronous coroutine that takes an integer argument (max_delay)
and waits for a random delay between 0 and max_delay (inclusive) seconds.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay
    seconds and return the delay.

    Args:
    max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
    float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
