import math

from error import calculate_absolute_relative_error_approx


class BisectionMethod:
    """
    Bisection Method solves any with single variable equation with defined set of
    """
    def __init__(self, f, x_low, x_high, epsilon, should_continue, maximum_iterations=math.inf, on_next=lambda x: None):
        self.f = f
        self.x_low = x_low
        self.x_high = x_high
        self.epsilon = epsilon
        self.should_continue = should_continue
        self.on_next = on_next
        self.maximum_iterations = maximum_iterations
        self.current_iteration = 0

        self.x = None
        self.x_old = None

    def solve_single_root(self):
        """
        Bisection method for solving a root of a function f
        """
        if self.f(self.x_low) * self.f(self.x_high) > 0:
            raise ValueError("f(a) and f(b) must have opposite signs")

        self.current_iteration = 0
        while self.current_iteration < self.maximum_iterations and self.should_continue(self):
            self.on_next(self)
            self.x_old = self.x
            self.x = (self.x_low + self.x_high) / 2
            if self.f(self.x) == 0:
                return self.x
            elif self.f(self.x) * self.f(self.x_low) < 0:
                self.x_high = self.x
            else:
                self.x_low = self.x

            self.current_iteration += 1

        return self.x


def absolute_relative_error_approx(b):
    """
    Continuity interceptor for bisection method based on absolute relative error
    approximation
    :param b: BisectionMethod object reference
    :return: whether bisection method should continue to find root
    """
    if b.x_old is None or b.x is None or b.x_old == 0:
        return True
    return calculate_absolute_relative_error_approx(b.x_old, b.x) > b.epsilon


"""
Continuity Interceptors for bisection method
These functions decide whether to continue to find root after each iteration
"""
continuity_interceptors = {
    'absolute_relative_error_approx': absolute_relative_error_approx
}
