def not_a_pep8_fn():
    print("Linter should error!")


class Example:
    def __init__(self):
        self.x = 6

    def wrong_func(self):
        print("Linter should error!")
