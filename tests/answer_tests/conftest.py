"""add path to sys path"""

import pytest
import time

from maths.logs import logging


@pytest.fixture
def solve_problem():
    def solve(problem_file):

        setup_start = time.perf_counter()
        problem = __import__(problem_file[:-3])
        setup_end = time.perf_counter()
        answer = problem.ANSWER
        solution_func = problem.solution
        setup_duration = setup_end - setup_start
        setup_msg = f"Setup duration = {setup_duration:0.4f} seconds"

        solution_start = time.perf_counter()
        solution = solution_func()
        solution_end = time.perf_counter()
        solution_duration = solution_end - solution_start
        solution_msg = f"Solution duration = {solution_duration:0.4f} seconds"

        if setup_duration > 1:
            logging.warning(setup_msg)
        if solution_duration > 1:
            logging.warning(solution_msg)

        assert solution == answer
        # print(
        #     f"success on {problem_file:50} in {solution_duration:0.4f} seconds"
        #     + f"{bypass_msg}{duration_str}{import_str}"
        # )

    return solve
