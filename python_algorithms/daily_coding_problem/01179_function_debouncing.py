"""
Given a function f, and N return a debounced f of N milliseconds.

That is, as long as the debounced f continues to be invoked, f itself 
will not be called for N milliseconds.
"""
import time
from threading import Timer
from typing import Callable


def debounce(func: Callable, delay: int) -> Callable:
    timer = None

    def wrapper(*args, **kwargs) -> None:
        nonlocal timer

        def call():
            nonlocal timer

            timer = None
            func(*args, **kwargs)

        if timer is None:
            call()
        else:
            if timer is not None:
                timer.cancel()

            timer = Timer(delay / 1000, call, *args, **kwargs)
            timer.start()

    return wrapper


def print_message(message: str) -> None:
    print(message)


if __name__ == "__main__":
    debounced = debounce(print_message, 1000)
    debounced("Hello")
    time.sleep(0.5)
    debounced("World")
    time.sleep(1.5)
    debounced("!")
