#!/usr/bin/env python3
"""
Module for measuring the execution time of the wait_n function.

This module provides a function `measure_time` that measures
the total execution time for the wait_n coroutine and returns
the average time per coroutine.
"""

import time
import importlib.util
import sys
import asyncio
from typing import List

# Dyn import wait_n function from 1-concurrent_coroutines.py
spec = importlib.util.spec_from_file_location(
    "wait_n", "./1-concurrent_coroutines.py"
)
wait_n_module = importlib.util.module_from_spec(spec)
sys.modules["1-concurrent_coroutines"] = wait_n_module
spec.loader.exec_module(wait_n_module)
wait_n = wait_n_module.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for the `wait_n` coroutine and calculates
    the average time per coroutine

    Args:
        n (int): The number of coroutines to execute.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        float: The average time per coroutine.
    """
    start_time = time.time()  # Record the start time

    # Call the wait_n coroutine and get the results
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()  # Record the end time

    total_time = end_time - start_time  # Calculate the total execution time

    # Return the average time per coroutine
    return total_time / n
