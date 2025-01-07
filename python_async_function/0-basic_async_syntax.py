#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that
waits for a random delay and returns the delay time.
"""

import random
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random
    delay between 0 and max_delay seconds and returns
    the delay.

    Args:
        max_delay (int): The maximum delay in seconds.
        Defaults to 10.

    Returns:
        float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)  # Generate a random float between 0 and max_delay
    await asyncio.sleep(delay)  # Asynchronously wait for the delay
    return delay  # Return the delay value
