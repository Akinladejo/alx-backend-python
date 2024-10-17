#!/usr/bin/env python3
"""
This module contains a coroutine that collects random
numbers using an async comprehension.
"""

from asyncio import sleep
from random import uniform
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return a list of values yielded by async_generator."""
    return [value async for value in async_generator()]
