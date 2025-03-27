import unittest
import importlib.util
import os


def load_communicating_vessels():
    file_path = os.path.join(os.path.dirname(__file__), '../src/5.4.communicating_vessels.py')  # Adjust if needed
    spec = importlib.util.spec_from_file_location("communicating_vessels", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.communicating_vessels


communicating_vessels = load_communicating_vessels()


class MyTestCase(unittest.TestCase):

    def test_basic_merge(self):
        result = list(communicating_vessels('ab', [1, 2, 3], ('@', '%')))
        self.assertEqual(result, ['a', 1, '@', 'b', 2, '%', 3])

    def test_single_iterable(self):
        result = list(communicating_vessels([10, 20, 30]))
        self.assertEqual(result, [10, 20, 30])

    def test_empty(self):
        result = list(communicating_vessels())
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
