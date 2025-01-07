#!/usr/bin/env python3
"""
Module for concurrent coroutines with async in Python.

This module provides a function `wait_n` that executes multiple
coroutines concurrently and returns their results in ascending order.
"""

import asyncio
from typing import List
import importlib.util
import sys


# Dynamically import the wait_random function from 0-basic_async_syntax.py
spec = importlib.util.spec_from_file_location(
    "wait_random", "./0-basic_async_syntax.py"
)
wait_random_module = importlib.util.module_from_spec(spec)
sys.modules["0_basic_async_syntax"] = wait_random_module
spec.loader.exec_module(wait_random_module)
wait_random = wait_random_module.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes `wait_random` coroutine `n` times concurrently
    with a specified `max_delay`.

    Args:
        n (int): The number of coroutines to execute.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = []

    for task in asyncio.as_completed(tasks):
        result = await task
        # Insert result into the list in sorted order
        if not results or result >= results[-1]:
            results.append(result)
        else:
            for i, value in enumerate(results):
                if result < value:
                    results.insert(i, result)
                    break
    return results
