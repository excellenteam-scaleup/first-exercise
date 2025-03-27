from functools import wraps


def surprise(func):
    @wraps(func)
    def wrapper():
        print("surprise!")

    return wrapper
