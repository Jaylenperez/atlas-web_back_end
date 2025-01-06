#!/usr/bin/env python3
"""
This module defines a function to sum a mixed list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums all elems in mixed list of ints and floats returns the result as float

    Args:
        mxd_lst (List[Union[int, float]]): List of ints and floats to sum.

    Returns:
        float: The sum of the integers and floats in the list.
    """
    return float(sum(mxd_lst))
