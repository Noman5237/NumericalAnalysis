import math
import unittest

from BisectionMethod import BisectionMethod, continuity_interceptors
from equation import generate_polynomial_equation


class BisectionMethodTest(unittest.TestCase):
    def test_single_root(self):
        root = BisectionMethod(lambda x: x ** 2 - 1,
                               -1, 1, 0.00001,
                               continuity_interceptors['absolute_relative_error_approx']
                               ).solve_single_root()
        self.assertAlmostEqual(root, math.sqrt(1), places=4)

        root = BisectionMethod(lambda x: x ** 3 - 2 * x ** 2 - 5 * x, -4, 4, 0.00001,
                               continuity_interceptors['absolute_relative_error_approx']
                               ).solve_single_root()
        self.assertAlmostEqual(root, 0, places=4)

        root = BisectionMethod(generate_polynomial_equation([1, -2, 0, 4]),
                               -2, 1, 0.001,
                               continuity_interceptors['absolute_relative_error_approx']
                               ).solve_single_root()
        self.assertAlmostEqual(root, -1.13, places=2)

        if __name__ == '__main__':
            unittest.main()
