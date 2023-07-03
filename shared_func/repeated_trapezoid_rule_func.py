#src video = https://www.youtube.com/watch?v=dDC2Kkw8YuM
import sympy as sp

def repeated_trapezoid_rule(f, a, b, desired_error):
    x = sp.Symbol('x')
    f_prime = f.diff(x)  # First derivative of f(x)

    n = 1  # Initial number of subintervals
    integral_prev = 0  # Integral value from previous iteration

    while True:
        h = (b - a) / n  # Width of each subinterval
        x_val = a
        integral = 0.5 * (f.subs(x, a) + f.subs(x, b))  # Initialize the integral with the endpoints

        for _ in range(1, n):
            x_val += h
            integral += f.subs(x, x_val)

        integral *= h

        if abs(integral - integral_prev) < desired_error:
            break

        n *= 2
        integral_prev = integral

    return integral

def calculate_cross_section_area(df, x="Distance_from_left_bank", y="Depth"):
    trapezoid_areas = []
    for i in range(len(df) - 1):
        area = 0.5 * (df[x].iloc[i+1] + df[x].iloc[i]) * (df[y].iloc[i+1] - df[y].iloc[i])
        trapezoid_areas.append(area)
    return trapezoid_areas

"""The formulas used in the trapezoid_rule function and the calculate_cross_section_area function are different because they serve different purposes.

In the trapezoid_rule function, the purpose is to numerically approximate the integral of a function using the trapezoid rule. The formula used in the trapezoid_rule function is derived from the trapezoid rule integration method, where the integral is approximated by dividing the interval into small trapezoids and summing their areas. The formula calculates the trapezoid areas based on the function values at specific points.

On the other hand, in the calculate_cross_section_area function, the purpose is to calculate the cross-sectional areas based on the provided data points in the DataFrame. The formula used in this function calculates the areas of trapezoids based on the differences in the x and y values of consecutive points in the DataFrame.

The formulas differ because they are designed to address different problems. The trapezoid rule integration method is used for numerical integration, while the calculation of cross-sectional areas involves the geometric interpretation of trapezoids based on given data points."""
