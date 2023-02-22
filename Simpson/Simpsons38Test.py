import math
import unittest

from Simpson38 import Simpson38


def velocity(t):
    return 2000 * math.log(140000 / (140000 - 2100 * t)) - 9.8 * t


class Simpsons38Test(unittest.TestCase):
    def test_simpsons38_integral(self):
        simpsons38 = Simpson38(velocity, 8, 30, 3)
        result = simpsons38.calculate_integral()

        self.assertAlmostEqual(result, 11603.31, places=2)

        if __name__ == '__main__':
            unittest.main()
