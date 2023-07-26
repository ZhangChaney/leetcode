#!/usr/bin/python3
# -*- coding:utf-8 -*-
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(f'method: {wrapper.__name__}')
        print(f'time consuming: {round(time.time() - start, 3)}s')
        print('-' * 50)

        return res

    return wrapper

