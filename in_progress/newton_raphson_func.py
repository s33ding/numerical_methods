import sympy as sp

C = 2
I = 0.83
Q0 = 7 * C
R = 3

expr = lambda x: (14 / R * C) * sp.E ** (-x / (R * C))
expr_prime = sp.diff(expr(sp.Symbol('x')), sp.Symbol('x'))

x0 = 0
epsilon = 1e-6  # Desired level of accuracy

while True:
    f_val = expr(x0)
    if abs(f_val) < epsilon:
        break

    f_prime_val = expr_prime.subs(sp.Symbol('x'), x0)
    x0 = x0 - f_val / f_prime_val

root = x0
print("The root of the equation is:", root)
