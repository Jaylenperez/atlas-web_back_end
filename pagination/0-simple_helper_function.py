#!/usr/bin/env python3
"""
Contains a helper function to calculate index range for pagination
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing the start and end index of a page in
    a paginated dataset

    The start index is calculated as (page - 1) * page_size, and the index is
    the start index plus page_size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and the end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
