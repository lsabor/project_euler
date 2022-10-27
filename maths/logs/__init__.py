""" logging stuff """


import logging
import sys
import os
import functools
import inspect
from typing import overload

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)


handler = logging.StreamHandler(sys.stderr)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

level_map = {
    "DEBUG": logger.debug,
    "INFO": logger.info,
    "WARNING": logger.warning,
    "ERROR": logger.error,
    "CRITICAL": logger.critical,
}


def log(*args, **kwargs):
    """Logs a function's call args and kwargs.
    Decorate function with @log or @log(kwarg = kwarg, ...).
    default logging level is DEBUG. To set higher, set
    level = "WARNING" for example.
    """

    level = kwargs.get("level", "DEBUG")
    logAtLevel = level_map[level]

    def logwrap(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            full_filename = inspect.stack()[1].filename
            filename = os.path.splitext(os.path.basename(full_filename))[0]
            callstring = (
                f" {filename}.{func.__qualname__} called with {args=},{kwargs=}"
            )
            try:
                result = func(*args, **kwargs)
                if result is not None:
                    logAtLevel(f"{callstring}: {result=}")
                else:
                    logAtLevel(f"{callstring}")
                return result
            except Exception as e:
                logAtLevel(callstring)
                logger.exception(
                    f"  Exception raised in {func.__qualname__}. exception: {str(e)}"
                )
                raise e

        return wrapper

    if not args:  # senses if log is being called on func, or with args
        return logwrap
    return logwrap(*args)
