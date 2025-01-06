#!/usr/bin/env python3
"""
This module provides a type-annotated function to compute the floor of a float.
"""


import math

def floor(n: float) -> int:
    """
    Returns the floor of a float number.

    Args:
        n (float): The float to floor.

    Returns:
        int: The floor of the float.
    """
    return math.floor(n)
