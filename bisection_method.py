import numpy as np
import pandas as pd

def calculate_tol(a, b, epsilon):
    """
    This function calculates the value of tol using the natural logarithm formula.

    Parameters:
    a (float): The left end point of the interval.
    b (float): The right end point of the interval.
    epsilon (float): The desired relative error.

    Returns:
    tol (float): The value of tol calculated using the natural logarithm formula.
    """

    tol = epsilon * np.log(abs(b - a) / np.finfo(float).eps)

    return tol

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    """
    This function implements the bisection method to find a root of a function f.

    Parameters:
    f (function): The function for which the root is to be found.
    a (float): The left end point of the interval.
    b (float): The right end point of the interval.
    tol (float, optional): The tolerance for the solution. Default is 1e-6.
    max_iter (int, optional): The maximum number of iterations. Default is 100.

    Returns:
    df (pandas.DataFrame): A DataFrame containing the results of the bisection method.
    """

    # Check if the signs of f(a) and f(b) are opposite
    if np.sign(f(a)) == np.sign(f(b)):
        print("Error: f(a) and f(b) must have opposite signs!")
        return None

    # Initialize variables
    i = 0
    fa = f(a)

    # Create pandas DataFrame to store results
    """
    The DataFrame has six columns:

    i: the iteration number
    a: the left endpoint of the interval
    b: the right endpoint of the interval
    xm: the midpoint of the interval
    f(xm): the value of the function at xm
    error: the absolute error, defined as |b - a
    """
    columns = ['i', 'a', 'b', 'xm', 'f(xm)', 'error']
    df = pd.DataFrame(columns=columns)

    # Implement bisection method
    while i < max_iter:
        # Calculate midpoint
        xm = (a + b) / 2

        # Evaluate function at midpoint
        fxm = f(xm)

        # Calculate absolute error
        error = abs((b - a) / 2)

        # Store results in DataFrame
        df = pd.concat([df, pd.DataFrame([[i, a, b, xm, fxm, error]], columns=columns)], ignore_index=True)

        # Check for convergence
        if fxm == 0 or error < tol:
            break

        # Update iteration count
        i += 1

        # Update interval
        if np.sign(fa) == np.sign(fxm):
            a = xm
            fa = fxm
        else:
            b = xm

    return df
