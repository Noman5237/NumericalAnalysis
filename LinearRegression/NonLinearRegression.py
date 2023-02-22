import math

from LinearRegression import LinearRegression


class NonLinearRegression:
    def __init__(self, x_arr, y_arr):
        self.x_arr = x_arr
        self.y_arr = y_arr
        self.A = 0
        self.l = 0

    def calculate_coefficients_lr_least_square(self):
        lr = LinearRegression(self.x_arr, self.y_arr);
        lr.calculate_coefficients_least_squares()
        a0, a1 = lr.c, lr.m
        self.A = math.exp(a0);
        self.l = a1

    def predict(self, x):
        return self.A * math.exp(self.l * x)
