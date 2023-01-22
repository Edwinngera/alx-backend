#!/usr/bin/env python3
'''
    Simple helper function.
'''


def index_range(page, page_size):
    '''
        Returns the range of indexes for a given page.
    '''
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
