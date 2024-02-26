from src.script1 import sum
import unittest

class TestSum(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(sum(1,2), 3)


if __name__ == "__main__":
    unittest.main()