class Simpson38:
    def __init__(self, function, min_x, max_x, n):
        self.function = function
        self.min_x = min_x
        self.max_x = max_x
        self.n = n
        self.h = (max_x - min_x) / n

    def calculate_segments(self):
        segments = [self.min_x + i * self.h for i in range(0, self.n + 1)]
        return segments

    def calculate_segments_values(self):
        segments = self.calculate_segments()
        values = [self.function(x) for x in segments]
        return values

    def calculate_integral(self):
        h = self.h
        min_y = self.function(self.min_x)
        max_y = self.function(self.max_x)

        values = self.calculate_segments_values()

        ones = [values[i] for i in range(1, self.n - 2 + 1, 3)]
        twos = [values[i] for i in range(2, self.n - 1 + 1, 3)]
        threes = [values[i] for i in range(3, self.n - 3 + 1, 3)]

        integral = (3 * h / 8) * (min_y + 3 * sum(ones) + 3 * sum(twos) + 2 * sum(threes) + max_y)

        return integral

    def calculate_errors_for_segment_values(self):
        values = self.calculate_segments_values()
        errors = []
        for i in range(1, self.n + 1):
            error = abs(values[i] - values[i - 1]) / values[i]
            errors.append(error)

        return errors
