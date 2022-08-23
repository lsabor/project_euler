"""add path to sys path"""

import sys
import os
import pytest
import time

from maths.logs import logger


def get_problem_files(section):
    sys.path.append(section)
    return [file for file in os.listdir(section) if file.endswith(".py")]


@pytest.fixture
def solve_problem():
    def solve(problem_file):
        problem = __import__(problem_file[:-3])
        answer = problem.ANSWER
        start = time.perf_counter()
        solution = problem.solution()
        end = time.perf_counter()
        assert solution == answer
        # logger.info(f"success on {problem_file:50} in {end - start: 0.4f} seconds")
        print(f"success on {problem_file:50} in {end - start: 0.4f} seconds")

    return solve
