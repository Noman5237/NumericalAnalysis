import math

from error import calculate_absolute_relative_error_approx


class SecantMethod:
    """
    Secant Method solves any with single variable equation with defined set of
    """

    def __init__(self, f, x0, x1, epsilon, should_continue, maximum_iterations=math.inf, on_next=lambda x: None):
        self.f = f
        self.x0 = x0
        self.x1 = x1
        self.epsilon = epsilon
        self.should_continue = should_continue
        self.on_next = on_next
        self.maximum_iterations = maximum_iterations
        self.current_iteration = 0

        self.x = None

    def solve_single_root(self):
        """
        Secant method for solving a root of a function f
        """
        self.current_iteration = 0
        while self.current_iteration < self.maximum_iterations and self.should_continue(self):
            self.on_next(self)
            if self.x is not None and self.x1 is not None:
                self.x0, self.x1 = self.x1, self.x
            self.x = self.x1 - self.f(self.x1) * (self.x1 - self.x0) / float(self.f(self.x1) - self.f(self.x0))
            self.current_iteration += 1

        return self.x


def absolute_relative_error_approx(b):
    """
    Continuity interceptor for secant method based on absolute relative error
    approximation
    :param b: SecantMethod object reference
    :return: whether secant method should continue to find root
    """
    if b.x is None or b.x1 is None:
        return True
    return calculate_absolute_relative_error_approx(b.x1, b.x) > b.epsilon


"""
Continuity Interceptors for secant method
These functions decide whether to continue to find root after each iteration
"""
continuity_interceptors = {
    'absolute_relative_error_approx': absolute_relative_error_approx
}
