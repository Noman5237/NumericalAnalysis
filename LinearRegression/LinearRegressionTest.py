import unittest

from LinearRegression import LinearRegression


class LinearRegressionTest(unittest.TestCase):
    def test_least_squares(self):
        time = [0, 1, 3, 5, 7, 9]
        gamma = [1, 0.891, 0.708, 0.562, 0.447, 0.355]
        lr = LinearRegression(time, gamma)
        lr.calculate_coefficients_least_squares()
        print(lr.m, lr.c)
        self.assertAlmostEqual(lr.m, -0.11505, places=5)
        self.assertAlmostEqual(lr.c, -2.6150 * 10 ** -4, places=5)


if __name__ == '__main__':
    unittest.main()
