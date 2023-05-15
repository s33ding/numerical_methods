#src: https://youtu.be/OO66Czt9rqg
import pandas as pd
import sympy as sp
#from newton_raphson_func import *
from shared_func.math_func import *
from shared_func.newton_raphson_func import *

# Example usage

lamb_expr = lambda x: 25 * x**2 + sp.log(x) - 1.5

f = create_a_math_function(lamb_expr)
f_diff = make_derivative_lambda(lamb_expr)

x = 1
tol = .1


matrix = newton_rathson(
    f=f, 
    f_diff=f_diff, 
    x=x, 
    tol=tol, 
    matrix=[], 
    fx=None)

df = pd.DataFrame(matrix)
df.index = "x" + df["index"].astype("str")
df.drop(columns = ["index"],inplace=True)
df['x'] = df['x'].apply(lambda x: round(x, 4) if pd.notnull(x) else x)
df['fx'] = df['fx'].apply(lambda x: round(x, 4) if pd.notnull(x) else x)
df['df_dx'] = df['df_dx'].apply(lambda x: round(x, 4) if pd.notnull(x) else x)
df['res'] = df['res'].apply(lambda x: round(x, 4) if pd.notnull(x) else x)
df['stop_criterion'] = df['stop_criterion'].apply(lambda x: round(x, 4) if pd.notnull(x) else x)
print(df)

