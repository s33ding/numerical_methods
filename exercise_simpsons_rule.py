
#extra source: https://www.youtube.com/watch?v=3-sssBS3TNU
import math
import numpy as np
from shared_func.simpsons_func import simpsons_1_3rd_rule

def function_to_integrate(x):
    # This is the function f(x) = sqrt(16 - x^2)
    return np.sqrt(16 - x**2)

#define the limits of integration and number of intervals
a = 0
b = 4
n = 10000

# you can choose n as you want, more the intervals, more precise the result

# calculate the integral and multiply by 2 to get the full circle's area
circle_area = simpsons_1_3rd_rule(function_to_integrate, a, b, n)
circle_area = circle_area
msg = f"Area: {circle_area} square meters."
print(msg)

