#!usr/bin/env python
"""
Simple helper function 

"""


def index_range(page, page_size):

    start=(page-1)*page_size
    end=page*page_size

    return start, end