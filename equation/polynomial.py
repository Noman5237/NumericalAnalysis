def generate_polynomial_equation(coefficients):
    def polynomial_function(x):
        result = 0
        for i in range(len(coefficients)):
            result += coefficients[i] * x ** (len(coefficients) - 1 - i)
        return result

    return polynomial_function
