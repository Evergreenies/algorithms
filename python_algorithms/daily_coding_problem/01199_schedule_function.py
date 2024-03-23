"""
Implement a job scheduler which takes in a function f and an integer n, 
and calls f after n milliseconds.
"""
import threading

from typing import Callable


class Scheduler:
    def __init__(self) -> None:
        self.jobs = []

    def schedule(self, func: Callable, delay: int) -> None:
        job = threading.Timer(delay / 1000.0, func)
        self.jobs.append(job)
        job.start()

    def wait(self) -> None:
        for job in self.jobs:
            job.join()


def function() -> None:
    print("Function called after specified delay.")


if __name__ == "__main__":
    scheduler = Scheduler()
    print("Function scheduled to execute after two seconds.")
    scheduler.schedule(function, 2000)
    scheduler.wait()
    print("Job finished.")
