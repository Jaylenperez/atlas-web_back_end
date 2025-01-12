#!/usr/bin/env python3
"""
Module: 0-async_generator
Provides an asynchronous generator that yields random numbers between 0 and 10.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random numbers between 0 and 10.

    This coroutine loops 10 times. In each iteration, it waits
    asynchronously for 1 second and then yields a random
    floating-point number in the range [0, 10].

    Returns:
        Generator[float, None, None]: An asynchronous
        generator yielding floats.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
