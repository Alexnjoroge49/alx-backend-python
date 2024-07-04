#!/usr/bin/env python3
"""
This is a module that provides a function for zooming in on a tuple.
"""
from typing import List, Tuple, Union


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    This function takes a tuple and a zoom factor, and returns a new list
        with the elements of the tuple repeated according to the zoom factor.

    Parameters:
    lst (Tuple[int, ...]): The tuple to zoom in on.
    factor (int): The zoom factor, which determines how many times each
        element of the tuple should be repeated in the output list.

    Returns:
    List[int]: A new list with the elements of the tuple repeated according to
        the zoom factor.
    """
    zoomed_in: List[int] = [
        item for _ in range(factor)
        for item in lst
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)

if __name__ == "__main__":
    print(zoom_array.__annotations__)
    print(zoom_2x)
    print(zoom_3x)

