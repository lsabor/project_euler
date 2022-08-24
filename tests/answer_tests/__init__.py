import sys
import os


def get_problem_files(section):
    sys.path.append(section)
    return [file for file in os.listdir(section) if file.endswith(".py")]
