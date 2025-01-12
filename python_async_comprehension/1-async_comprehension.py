#!/usr/bin/env python3
"""
Module: 1-async_comprehension
Defines a coroutine to collect random numbers using an async comprehension.
"""

from typing import List
import importlib

# Dynamically import async_generator from 0-async_generator
async_generator = importlib.import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehension over
    async_generator.

    The coroutine asynchronously iterates over async_generator, collecting
    10 random numbers into a list, and then returns the list.

    Returns:
        List[float]: A list of 10 random floating-point numbers.
    """
    return [number async for number in async_generator()]
