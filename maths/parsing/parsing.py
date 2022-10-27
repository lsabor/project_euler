# This module holds basic parsing functions


from pathlib import Path
import inspect


def get_problem_file_from_number(number) -> Path:
    root = Path("./problem_files")
    return next(root.glob("*" + number + "*"))


def auto_get_problem_file() -> Path:
    filename = inspect.stack()[1].filename
    file = filename.split("/")[-1]
    problem_number = file[:3]
    return get_problem_file_from_number(problem_number)


def read_file_as_array(file) -> list:
    arr = [[int(value) for value in a.strip().split(",")] for a in file]
    return arr


def readArrayStr(array: str) -> list:
    # returns a list of lists, each contained list is a row of array
    array = array.strip()
    arr = array.split("\n")
    arr = [[int(value) for value in a.strip().split(" ")] for a in arr]
    return arr
