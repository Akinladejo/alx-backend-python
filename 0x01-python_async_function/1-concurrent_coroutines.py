#!/usr/bin/env python3
"""
Import wait_random from the previous python file that
you’ve written and write an async routine called wait_n
that takes in 2 int arguments: max_delay and n. You will
spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values)
The list of the delays should be in ascending order without
using sort() because of concurrency.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Waits for a random delay until max_delay, returns
        a list of actual delays.

    Args:
    n (int): The number of times to call wait_random.
    max_delay (int): The maximum delay for wait_random.

    Returns:
    List[float]: A list of all delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
