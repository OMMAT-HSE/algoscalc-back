import unittest


from src.algorithms.fast_fibonacci.function import *


class TestCase(unittest.TestCase):
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    def test_fibonacci(self):
        for index, number in enumerate(self.numbers):
            self.assertEqual(main(str(index + 1)), {'result': str(number)})

    def test_matrix_mul_1(self):
        self.assertEqual((5, 8), mulmatrix2x1((2, 1), (1, 2, 3, 4)))

    def test_matrix_mul_2(self):
        self.assertEqual((5, 8, 7, 10), mulmatrix2x2((2, 1, 1, 2), (1, 2, 3, 4)))


if __name__ == '__main__':
    unittest.main()
