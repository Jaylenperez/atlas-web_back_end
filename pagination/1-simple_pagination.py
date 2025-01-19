#!/usr/bin/env python3
"""
Contains a class Server to paginate a dataset of popular baby names.
"""

import csv
import math
from typing import List


# Reusing index_range from the previous task
def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing the start and end index
    of a page in a paginated dataset.

    The start index is calculated as (page - 1) * page_size,
    and the end index is the start index plus page_size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and
        the end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Returns the cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skipping header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the appropriate page of the dataset based
        on the page and page_size.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows corresponding to the requested page.
        """
        # Validate that the page and page_size are positive integers
        assert isinstance(page, int), "page must be an integer"
        assert isinstance(page_size, int), "page_size must be an integer"
        assert page > 0, "page must be greater than 0"
        assert page_size > 0, "page_size must be greater than 0"

        # Use the index_range function to calculate the correct indices
        start_index, end_index = index_range(page, page_size)

        # Get the dataset
        dataset = self.dataset()

        # Return the correct page of the dataset,
        # or an empty list if out of range
        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
