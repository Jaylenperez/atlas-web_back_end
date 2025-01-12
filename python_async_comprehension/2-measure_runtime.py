#!/usr/bin/env python3
"""
Module: 2-measure_runtime
Defines a coroutine to measure the runtime of
executing async_comprehension four times in parallel.
"""

import asyncio
import time
import importlib

# Dynamically import async_comprehension from 1-async_comprehension
async_comprehension = importlib.import_module(
    '1-async_comprehension'
).async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of executing async_comprehension
    four times in parallel.

    The coroutine uses asyncio.gather to run four parallel instances of
    async_comprehension. Since the comprehensions execute concurrently, the
    total runtime should be approximately 10 seconds, not 40 seconds.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()  # Record start time

    # Explicitly call asyncio.gather
    tasks = [
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    ]
    await asyncio.gather(*tasks)

    end_time = time.perf_counter()  # Record end time
    return end_time - start_time
