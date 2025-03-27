import time

"""
Checks runtime of a function
"""


def running_2000(f, *args, **kwargs):
    start = time.perf_counter()
    f(*args, **kwargs)
    return (time.perf_counter() - start)


def main():
    # Code here:
    ""


if __name__ == "__main__":
    main()
