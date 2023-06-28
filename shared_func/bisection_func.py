import math as mt
import numpy as np
from  shared_func.bolzano_func import bolzano 
import pandas as pd


def get_the_midpoint(a, b):
    """
    Calculates the midpoint of an interval.

    Args:
        a, b: The endpoints of the interval.

    Returns:
        The midpoint of the interval.

    """
    # Calculate the midpoint as the average of the endpoints
    midpoint = (a + b) / 2
    
    # Return the midpoint
    return midpoint


def k(a, b, tol):
    """
    Calculates the number of iterations required for the bisection method to achieve a certain tolerance.

    Args:
        a, b: The endpoints of the interval to search for a root.
        tol: The tolerance for the root, i.e., the desired accuracy.

    Returns:
        The number of iterations required to achieve the given tolerance.

    """
    # Calculate the logarithm of the interval size and the tolerance, and use them to determine the number of iterations
    log_size = mt.log(b - a)
    log_tol = mt.log(tol)
    num_iterations = (log_size - log_tol) / mt.log(2)
    
    # Return the ceiling of the number of iterations, which is the smallest integer greater than or equal to the number
    return mt.ceil(num_iterations)


def find_the_root_side(f, a, x0, b):
    """Finds the side of the root for a continuous function `f` on the interval [a, b].
    
    Args:
        f: A continuous function.
        a, b: The endpoints of the interval to search for a root.
        x0: The midpoint of the interval.
    
    Returns:
        The endpoints `a` and `b`, the function values `f(a)` and `f(x0)`, and the signal indicating the side of the root (+ or -).
    
    Example usage:
        >>> f = lambda x: x**2 - 3
        >>> a, b, fa, fx0, signal = find_the_root_side(f, 1, 2, 1.5)
        f(a): -2
        fx0: 0.25
        SIGNAL: -
        >>> a, b, fa, fx0, signal = find_the_root_side(f, 1.5, 2, 1.75)
        f(a): 0.25
        fx0: -1.0625
        SIGNAL: +
    
    """
    fx0 = f(x0)
    fa = f(a)
    print("f(a):", fa)
    print("fx0:", fx0)
    if fa * fx0 < 0:
        signal = "-"
        a = a
        b = x0
    else:
        signal = "+"
        print("SIGNAL: +")
        a = x0
        b = b

    print(f"SIGNAL: {signal}")
    return a, b, fa, fx0, signal

def bissection(f, a, b, tol, max_iter, n_iter=0, matrix=[]):
    """Finds a root of a continuous function `f` on the interval [a, b] using the bisection method.
    
    Args:
        f: A continuous function.
        a, b: The endpoints of the interval to search for a root.
        tol: The tolerance for the root, i.e., the desired accuracy.
        max_iter: The maximum number of iterations to perform.
        n_iter: The number of iterations performed so far (default 0).
        matrix: A list of intermediate results (default empty list).
    
    Returns:
        The endpoints `a` and `b` of the final interval, and a list of intermediate results in a pandas DataFrame.
    
    Example usage:
        >>> f = lambda x: x**2 - 3
        >>> a, b, matrix = bissection(f, 1, 2, 1e-6, 50)
        =========P1-GET_THE_MID_POINT=========
        max_iter=50;numb_of_iter=0
        a: 1
        b: 2
        x0: 1.5
        =========P2-FINDING THE ROOT SIDE=========
        =========P3-STOP CRITERION=========
        E(b-a)=0.5
        ...
    
    """
    print("==================")
    print("P1-GET THE MID POINT:")
    print(f"max_iter={max_iter};numb_of_iter={n_iter}")
    x0 = get_the_midpoint(a, b)
    print("a:", a)
    print("b:", b)
    print("x0:", x0)
    print("==================")
    print("P2-FINDING THE ROOT SIDE:")
    a, b, fa, fx0, signal = find_the_root_side(f=f, a=a, x0=x0, b=b)
    print("==================")
    print("P3-STOP CRITERION:")
    erro = b - a
    print(f"E(b-a)={erro}")
    n_iter += 1
    row = {"a": a, "b": b, "x0": x0, "fa": fa, "fx0": fx0, "signal": signal, "erro": erro}
    matrix.append(row)
    if n_iter >= max_iter or erro < tol:
        return a, b, pd.DataFrame(matrix)
    else:
        a, b, matrix = bissection(f, a, b, tol, max_iter, n_iter, matrix)
        return a, b, matrix

def find_root_bisection(f, a, b, tol):
    """
    Finds the root of a continuous function `f` on the interval [a, b] using the bisection method.

    Args:
        f: A continuous function.
        a, b: The endpoints of the interval to search for a root.
        tol: The tolerance for the root, i.e., the desired accuracy.

    Returns:
        A DataFrame containing the bisection method iteration results if a root is found, or None if no root exists.

    """
    # Check if the function has opposite signs at the endpoints using the Bolzano theorem
    test_of_bolzano = bolzano(f, a, b)
    if test_of_bolzano:
        print("It is negative, so a root exists.")
        # If a root exists, print a message and start the bisection method
        print("STARTING THE BISECTION METHOD:")
        max_iter = k(a, b, tol)
        a, b, matrix = bissection(f, a, b, tol, max_iter, n_iter=0)
        # Print the final result and return the DataFrame of iteration results
        print("=========FINAL RESULT=========")
        print(f"x = {(a+b)/2}")
        df = pd.DataFrame(matrix)
        print(df.head(50))
        return df
    else:
        # If no root exists, print a message and return None
        print("It is positive, so no root exists.")
        return None

