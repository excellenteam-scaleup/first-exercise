import unittest
import importlib.util
import os


def load_parsle_tongue():
    file_path = os.path.join(os.path.dirname(__file__), '../src/5.3.parsle_tongue.py')  # Adjust path if needed
    spec = importlib.util.spec_from_file_location("parsle_tongue", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.parsle_tongue


parsle_tongue = load_parsle_tongue()


class MyTestCase(unittest.TestCase):

    def test_hidden_words_found(self):
        result = parsle_tongue()

        expected_words = ['python', 'isawesome', 'welldone', 'goodjob']

        for word in expected_words:
            self.assertIn(word, result)


if __name__ == '__main__':
    unittest.main()
