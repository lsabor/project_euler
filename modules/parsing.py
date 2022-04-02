# This module holds basic parsing functions


def read_array_str(array: str) -> list:
    # returns a list of lists, each contained list is a row of array
    array = array.strip()
    arr = array.split('\n')
    arr = [[int(value) for value in a.strip().split(' ')] for a in arr]
    return(arr)





