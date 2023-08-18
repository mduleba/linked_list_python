from time import time
import logging


def timer_factory(comment):
    def timer(function):
        def wrapper(*args, **kwargs):
            start_time = time()
            result = function(*args, **kwargs)
            end_time = time()
            print(f'{comment}: executed in {(end_time - start_time):.10f}s')
            return result
        return wrapper
    return timer