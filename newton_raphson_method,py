import numpy as np
import pandas as pd

def newton_raphson_method(f, x0, tol=1e-6, max_iter=100):
    """
    This function implements the Newton-Raphson method to find a root of a function f.

    Parameters:
    f (function): The function for which the root is to be found.
    x0 (float): The initial guess for the root.
    tol (float, optional): The tolerance for the solution. Default is 1e-6.
    max_iter (int, optional): The maximum number of iterations. Default is 100.

    Returns:
    df (pandas.DataFrame): A DataFrame containing the results of the Newton-Raphson method.
    """

    # Initialize variables
    i = 0
    x = x0

    # Create pandas DataFrame to store results
    """
    The DataFrame has five columns:

    i: the iteration number
    x: the estimate of the root
    f(x): the value of the function at x
    f'(x): the derivative of the function at x
    error: the absolute error, defined as |x_{i+1} - x_i|
    """
    columns = ['i', 'x', 'f(x)', "f'(x)", 'error']
    df = pd.DataFrame(columns=columns)

    # Implement Newton-Raphson method
    while i <= max_iter:
        # Evaluate function and derivative at current estimate
        fx = f(x)
        fx_prime = (f(x + tol) - f(x - tol)) / (2 * tol)

        # Calculate new estimate of root
        x_new = x - fx / fx_prime

        # Calculate absolute error
        error = abs(x_new - x)

        # Store results in DataFrame
        df = pd.concat([df, pd.DataFrame([[i, x, fx, fx_prime, error]], columns=columns)], ignore_index=True)

        # Check for convergence
        if fx == 0 or error < tol or i == max_iter:
            break

        # Update iteration count and estimate of root
        i += 1
        x = x_new

    # Append final iteration to DataFrame if necessary
    if i == max_iter:
        fx = f(x)
        fx_prime = (f(x + tol) - f(x - tol)) / (2 * tol)
        error = abs(x_new - x)
        df = pd.concat([df, pd.DataFrame([[i, x, fx, fx_prime, error]], columns=columns)], ignore_index=True)

    return df
