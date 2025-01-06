#!/usr/bin/env python3
"""
Module defines a function to sum a list of floats and return result as float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums all elements in a list of floats and returns result as float.

    Args:
        input_list (List[float]): The list of floats to sum.

    Returns:
        float: The sum of the floats in the list.
    """
    return sum(input_list)
