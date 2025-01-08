#!/usr/bin/env python3
"""Module for creating asyncio tasks."""

import asyncio
import importlib

# Dynamically import the module
basic_async_syntax = importlib.import_module("0-basic_async_syntax")
wait_random = basic_async_syntax.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: A task that wraps the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
