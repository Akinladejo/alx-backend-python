#!/usr/bin/env python3

""" Async Comprehensions """

from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Asynchronously generates random floats between 0 and 10. """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
