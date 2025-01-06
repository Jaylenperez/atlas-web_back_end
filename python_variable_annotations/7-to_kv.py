#!/usr/bin/env python3
"""
This module defines a function to_kv, which returns a tuple.
The tuple contains a string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is a string k
    the second element is the square of v (which can be int or float),
    annotated as a float.

    Args:
        k (str): The string value.
        v (Union[int, float]): The value to be squared,
        either int or float.

    Returns:
        Tuple[str, float]: A tuple with the string and the square
        of the number (as float).
    """
    return (k, float(v ** 2))
