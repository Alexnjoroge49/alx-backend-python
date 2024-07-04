#!/usr/bin/env python3
"""
This is a module that provides a function for zooming in on a tuple.
"""
from typing import List, Tuple

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    This function takes a tuple and a zoom factor, and returns a new list
    with the elements of the tuple repeated according to the zoom factor.

    Parameters:
    lst (Tuple): The tuple to zoom in on.
    factor (int): The zoom factor, which determines how many times each
        element of the tuple should be repeated in the output list.

    Returns:
    List: A new list with the elements of the tuple repeated according to
        the zoom factor.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)

# :man: Author and Credits.
# This project was done by [SE. Moses Mwangi](https://github.com/MosesSoftEng). Feel free to get in touch with me;
# 
# :iphone: WhatsApp [+254115227963](https://wa.me/254115227963)
# 
# :email: Email [moses.soft.eng@gmail.com](mailto:moses.soft.eng@gmail.com)
# 
# :thumbsup: A lot of thanks to [ALX-Africa Software Engineering](https://www.alxafrica.com/) program for the project requirements.

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)

bob@dylan:~$ mypy 102-type_checking.py
Success: no issues found in 1 source file
bob@dylan:~$ cat 102-main.py 
#!/usr/bin/env python3

zoom_array = __import__('102-type_checking').zoom_array

print(zoom_array.__annotations__)

bob@dylan:~$ ./102-main.py 
{'lst': typing.Tuple[int, ...], 'factor': <class 'int'>, 'return': typing.List[int]}

