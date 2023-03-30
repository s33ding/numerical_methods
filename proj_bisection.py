import numpy as np
import matplotlib.pyplot as plt
from bisection_method import bisection_method



def introduction():
    code = """CODE
------------------------------------
# The company estimates that demand for the product is given by the following function:
def demand(price):
    return 100 - 2*price

# The company's cost function is given by:
def cost(quantity):
    return 20 + 5*quantity

# The company's profit function is given by:
def profit(price):
    quantity = demand(price)
    return quantity * price - cost(quantity)

# We want to find the price that maximizes profit, which can be done by finding the root of the derivative of profit:
def derivative_profit(price):
    h = 1e-6
    return (profit(price+h) - profit(price-h)) / (2*h)

# Use the bisection method to find the root of the derivative of profit
tol = 1e-6
max_iter = 100
a = 0
b = 50

df = bisection_method(derivative_profit, a, b, tol, max_iter)
print(df)
price_optimal = df['xm'].iloc[-1]
print(f"The optimal price point is ${price_optimal:.2f} per unit.")
------------------------------------
"""

    print(code)
    print("Welcome to my bisection method program!\n")
    print("This program uses the bisection method to solve a real-world problem: determining the optimal price of a product based on a demand function.\n")

    print("Here's what the `proj_bissection.py` script does:")
    print("- First, it imports the `bisect()` function from the `scipy.optimize` module, which is used to find the root of a function.")
    print("- Then, it defines a demand function `demand(q)` that takes a quantity `q` as input and returns the corresponding price `p`.")
    print("- Next, it defines a cost function `cost(q)` that takes a quantity `q` as input and returns the corresponding cost `c`.")
    print("- Using these functions, it defines a profit function `profit(q)` that takes a quantity `q` as input and returns the corresponding profit `p*q - c*q`.")
    print("- Finally, it uses the bisection method to find the quantity `q` that maximizes profit, and then calculates the corresponding price and profit.")
    print("\nLet's run the `proj_bissection.py` script now:\n")

# Context: A company is planning to launch a new product and wants to determine the optimal price point.

# The company estimates that demand for the product is given by the following function:
def demand(price):
    return 100 - 2*price

# The company's cost function is given by:
def cost(quantity):
    return 20 + 5*quantity

# The company's profit function is given by:
def profit(price):
    quantity = demand(price)
    return quantity * price - cost(quantity)

# We want to find the price that maximizes profit, which can be done by finding the root of the derivative of profit:
def derivative_profit(price):
    h = 1e-6
    return (profit(price+h) - profit(price-h)) / (2*h)

introduction()
# Use the bisection method to find the root of the derivative of profit
tol = 1e-6
max_iter = 100
a = 0
b = 50

df = bisection_method(derivative_profit, a, b, tol, max_iter)
print(df)
price_optimal = df['xm'].iloc[-1]

print(f"The optimal price point is ${price_optimal:.2f} per unit.")
