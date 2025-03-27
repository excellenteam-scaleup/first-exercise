from functools import wraps


class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def type_check(correct_type):
    def decorator_factory(func):
        @wraps(func)
        def wrapper(param):
            if not isinstance(param, correct_type):
                raise CustomError("wrong type, should be " + str(correct_type))
            return func(param)

        return wrapper

    return decorator_factory


@type_check(int)
def times2(num):
    return num * 2


# this code depends on closures to preserve metadata
# in summary something like this happens: wrapper(decorator_factory(func(param)))

def main():
    # Code here:
    ""


if __name__ == "__main__":
    main()
