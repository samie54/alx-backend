#!/usr/bin/env python3
"""
Contains - definition of index_range helper functionn.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes 2 integer arguments; returns a tuple of size two
    containing; start and end index correspondingg to range of
    indexes; to return in a listt for those pagination parameters
    Args:
        page (int): page number to return (pages are 1-indexed)
        page_size (int): number of items per page
    Return:
        tuple(start_index, end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
