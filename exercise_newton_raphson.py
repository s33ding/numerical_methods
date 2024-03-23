#src: https://youtu.be/OO66Czt9rqg
import pandas as pd
import sympy as sp
#from newton_raphson_func import *
from shared_func.math_func import *
from shared_func.newton_raphson_func2 import *

dfs = []
x = sp.symbols('x')
expr = 80 + 90 * sp.cos((sp.pi / 3) * x)


df, approx_solution = newton_raphson(
    f=sp.lambdify(x, expr),
    f_diff=sp.lambdify(x, sp.diff(expr, x)),
    x_val = 4,
    iter_count=0,
    max_iter=4,
    tol=0.0001
)

print("Approximate solution:", approx_solution)
print("\nIteration process:")
print(df.reset_index(drop=True))
dfs.append(df)
# Read CSS file
with open('media/style.css', 'r') as f:
    css = f.read()

# Write HTML file
with open('media/ap2-ex2.html', 'w') as f:
    f.write('<html>\n<head>\n')
    f.write(f'<style>\n{css}\n</style>\n')
    f.write('</head>\n<body>\n')
    f.write('<h1>Exercise 2</h1>\n')
    for df in dfs:
        title = "AP2-EX:2"
        f.write(f"<h4>{title}</h4>")
        f.write(f"<p>X = {df['x'].iloc[-1]}</p>")
        f.write(df.to_html(index=False))
    f.write('</body>\n</html>\n')

