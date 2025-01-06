#!/usr/bin/env python3
"""
Module defines function make_multiplier that returns a multiplier function.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a specified multiplier.
    
    Args:
        multiplier (float): The value to multiply by.
    
    Returns:
        Callable[[float], float]: Function that multiplies float by the multiplier.
    """
    # The returned function multiplies its argument by the multiplier
    def multiplier_function(n: float) -> float:
        return n * multiplier

    return multiplier_function
