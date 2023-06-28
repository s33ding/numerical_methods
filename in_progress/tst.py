import sympy as sp
import pandas as pd

def newton_raphson(f, f_diff, x_old, iter_count, max_iter, tol):
    f_val = f(x_old)
    f_diff_val = f_diff(x_old)

    x_new = x_old - f_val / f_diff_val

    data = {'Iteration': [iter_count],
            'x': [x_old],
            'f(x)': [f_val],
            "f'(x)": [f_diff_val],
            'x_new': [x_new],
            '|x_new - x|': [abs(x_new - x_old)]}

    df = pd.DataFrame(data)

    if abs(x_new - x_old) < tol or iter_count >= max_iter:
        return df, x_new
    else:
        recursive_df, solution = newton_raphson(f, f_diff, x_new, iter_count + 1, max_iter, tol)
        return pd.concat([df, recursive_df]), solution


print("-----------------------------------------------")
x = sp.symbols('x')

C = 2
I = 0.83
Q0 = 7 * C
R = 3

expr = lambda x: (Q0 / R * C) * sp.exp(-x / (R * C))

df, approx_solution = newton_raphson(
    f=sp.lambdify(x, expr),
    f_diff=sp.lambdify(x, sp.diff(expr, x)),
    x_old=0.5,
    iter_count=0,
    max_iter=100,
    tol=0.0001
)

print("Approximate solution:", approx_solution)
print("\nIteration process:")
print(df.reset_index(drop=True))
