import sympy as sp
import math as mt
from shared_func.repeated_trapezoid_rule_func import repeated_trapezoid_rule

# Define the function and its derivative
x = sp.Symbol('x')
f = mt.e**(2*x)
a = 1
b = 2
desired_error = 0.000001

# Calculate the integral
integral = repeated_trapezoid_rule(f, a, b, desired_error)
print("Approximate integral:", integral)

