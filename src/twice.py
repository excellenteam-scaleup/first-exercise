from decorator import decorator

"""
Decorator to call func twice
"""


@decorator
def twice(func, *args, **kwargs):
    for _ in range(2):
        func(*args, **kwargs)


def main():
    # Code here:
    ""


if __name__ == "__main__":
    main()
