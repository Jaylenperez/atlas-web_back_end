#!/usr/bin/env python3
"""Module for task_wait_n function."""

import asyncio
import importlib

# Dynamically import task_wait_random
tasks_module = importlib.import_module("3-tasks")
task_wait_random = tasks_module.task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """
    Executes multiple task_wait_random coroutines concurrently.

    Args:
        n (int): Number of tasks to run.
        max_delay (int): Maximum delay for each task.

    Returns:
        list[float]: List of delays in ascending order.
    """
    # Create and start all tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    # Wait for all tasks to complete and gather results
    delays = await asyncio.gather(*tasks)
    # Sort the results
    return sorted(delays)
