import numpy as np

def simpsons_1_3rd_rule(f, a, b, n):
    # This function implements Simpson's 1/3 rule for approximation of definite integrals
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    return h / 3 * (f(a) + f(b) + 4 * np.sum(f(x[1:-1:2])) + 2 * np.sum(f(x[2:-1:2])))
