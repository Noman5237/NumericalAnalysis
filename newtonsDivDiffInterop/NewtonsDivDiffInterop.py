def nearest_points(x_arr, y_arr, n, x_new):
    # Form a dictionary from x_arr and y_arr
    points = dict(zip(x_arr, y_arr))
    x_diff = {}
    for x in x_arr:
        x_diff[x] = abs(x_new - x)

    x_arr = sorted(x_arr, key=lambda elem: x_diff[elem])

    x_near = x_arr[:n]
    y_near = [points[x] for x in x_near]

    return x_near, y_near


def calculate_divided_difference_table(x_arr, y_arr):
    table = []
    n = len(x_arr)
    table.append(y_arr)
    for i in range(1, n):
        row = []
        for j in range(n - i):
            row.append((table[i - 1][j + 1] - table[i - 1][j]) / (x_arr[j + i] - x_arr[j]))
        table.append(row)

    return table


def get_coefficients(table):
    coefficients = []
    for i in range(len(table)):
        coefficients.append(table[i][0])
    return coefficients


def ndd(x_arr, y_arr, n, x_new):
    x_near, y_near = nearest_points(x_arr, y_arr, n, x_new)
    divided_difference_table = calculate_divided_difference_table(x_near, y_near)
    coefficients = get_coefficients(divided_difference_table)

    y_new = 0
    for i in range(n):
        term = coefficients[i]
        for j in range(i):
            term *= (x_new - x_near[j])
        y_new += term

    return y_new


def main():
    time_arr = [0, 10, 15, 20, 22.5, 30]
    velocity_arr = [0, 227.04, 362.78, 517.35, 602.97, 901.67]
    t_near, v_near = nearest_points(time_arr, velocity_arr, 4, 16)
    print(t_near, v_near)
    y = ndd(time_arr, velocity_arr, 4, 16)
    print(y)


if __name__ == '__main__':
    main()
