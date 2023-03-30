import numpy as np
import pandas as pd

def calculate_max_iter(a, b, tol):
    """
    Calculates the maximum number of iterations for the bisection method
    based on the given interval and tolerance using the formula:
    max_iter = ceil(log2((b - a)/tol))

    Parameters:
    a (float): The left endpoint of the interval.
    b (float): The right endpoint of the interval.
    tol (float): The tolerance for the solution.

    Returns:
    max_iter (int): The maximum number of iterations.
    """
    return int(np.ceil(np.log2((b - a) / tol)))

def bisection_method(f, a, b, tol=1e-6):
    """
    This function implements the bisection method to find a root of a function f.

    Parameters:
    f (function): The function for which the root is to be found.
    a (float): The left end point of the interval.
    b (float): The right end point of the interval.
    tol (float, optional): The tolerance for the solution. Default is 1e-6.

    Returns:
    df (pandas.DataFrame): A DataFrame containing the results of the bisection method.
    """
    max_iter=calculate_max_iter(a, b, tol)
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
    error: the absolute error, defined as |b - a|
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

    # Add the last row to the DataFrame
    xm = (a + b) / 2
    fxm = f(xm)
    error = abs((b - a) / 2)
    df = pd.concat([df, pd.DataFrame([[i+1, a, b, xm, fxm, error]], columns=columns)], ignore_index=True)

    return df
