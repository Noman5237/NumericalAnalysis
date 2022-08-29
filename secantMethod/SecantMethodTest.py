import unittest

from SecantMethod import SecantMethod, continuity_interceptors
from equation import generate_polynomial_equation


class SecantMethodTest(unittest.TestCase):
    def test_single_root(self):
        root = SecantMethod(generate_polynomial_equation([0.5, 0, -2, 5]),
                            2, 3, 0.01,
                            continuity_interceptors['absolute_relative_error_approx']) \
            .solve_single_root()
        print(root)
        self.assertAlmostEqual(root, -2.76, places=2)

        if __name__ == '__main__':
            unittest.main()
