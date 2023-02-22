import math


class LinearRegression:
    def __init__(self, x_arr, y_arr):
        self.x_arr = x_arr
        self.y_arr = y_arr
        self.c = None
        self.m = None

    def calculate_coefficients_least_squares(self):
        # Calculate the value of m using least squares method
        n = len(self.x_arr)
        self.y_arr = [math.log(y) for y in self.y_arr]
        sum_x = sum(self.x_arr)
        sum_y = sum(self.y_arr)
        sum_xy = sum([self.x_arr[i] * self.y_arr[i] for i in range(n)])
        sum_x2 = sum([x ** 2 for x in self.x_arr])
        numerator = n * sum_xy - sum_x * sum_y
        denominator = n * sum_x2 - sum_x ** 2
        self.m = numerator / denominator

        # Calculate the value of c using least squares method
        avg_x = sum_x / n
        avg_y = sum_y / n
        self.c = avg_y - self.m * avg_x
