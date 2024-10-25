import unittest
import numpy as np

from calc import add_matrices, subtract_matrices, multiply_matrices


class TestScientificCalculator(unittest.TestCase):

    def test_add_matrices(self):
        m1 = np.array([[1, 2], [3, 4]])
        m2 = np.array([[1, 2], [3, 4]])

        res = add_matrices(m1, m2)

        np.testing.assert_array_equal(res, np.array([[2, 4], [6, 8]]))

    def test_subtract_matrices(self):
        m1 = np.array([[1, 2], [3, 4]])
        m2 = np.array([[1, 2], [3, 4]])

        res = subtract_matrices(m1, m2)

        np.testing.assert_array_equal(res, np.array([[0, 0], [0, 0]]))

    def test_multiply_matrices(self):
        m1 = np.array([[1, 2], [3, 4]])
        m2 = np.array([[1, 2], [3, 4]])

        res = multiply_matrices(m1, m2)

        np.testing.assert_array_equal(res, np.array([[7, 10], [15, 22]]))


if __name__ == '__main__':
    unittest.main()
