# Given the ordinary differential equation
# $ \frac{d^2y}{dt^2}+2\frac{dy}{dt}+y=e^{-t}, y(0)=1, \frac{dy}{dt}(0)=2 $

import math


def f1(t, y, z):
    return z


def f2(t, y, z):
    return -2 * z - y + math.exp(-t)


# Runge-Kutta method using Heun's method
def runge_kutta_second_order_differential_equation(_f1, _f2, y0, z0, t0, t1, h, on_step=lambda t, y, z: None):
    t = t0
    y = y0
    z = z0
    while t < t1:
        k1 = h * _f1(t, y, z)
        z1 = h * _f2(t, y, z)
        k2 = h * _f1(t + h, y + k1, z + z1)
        z2 = h * _f2(t + h, y + k1, z + z1)
        y += (k1 + k2) / 2
        z += (z1 + z2) / 2
        t += h
        on_step(t, y, z)
    return y


def generate_curve(_f1, _f2, y0, z0, t0, t1, h):
    ys = []
    ts = []
    runge_kutta_second_order_differential_equation(_f1, _f2, y0, z0, t0, t1, h,
                                                   lambda t, y, z: (ys.append(y), ts.append(t)))
    return ts, ys


if __name__ == '__main__':
    print(runge_kutta_second_order_differential_equation(f1, f2, 1, 2, 0, 0.75, 0.25))
    ts, ys = generate_curve(f1, f2, 1, 2, 0, 0.75, 0.25)
    # generate matplotlib plot
    import matplotlib.pyplot as plt
    plt.plot(ts, ys)

