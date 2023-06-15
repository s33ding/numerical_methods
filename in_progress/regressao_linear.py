import math as mt
import pandas as pd

data =  {
            'x':[
                14, 
                6,
                3,
                6, 
                7, 
                6, 
                7,
                4, 
                8, 
                7, 
                6,
                4],
            'y':[
                10, 
                26, 
                41, 
                29, 
                27, 
                27,
                19, 
                28, 
                19, 
                31, 
                29, 
                33]
        }

df = pd.DataFrame(data)
df['x*y'] = df.x * df.y
df['x**2'] = df.x **2


sum_x= df.x.sum()

sum_y = df.y.sum()

sum_xy =df['x*y'].sum()

sum_xx=df['x**2'].sum()

n = len(df)
def f_coef_ang():
    print("({n} * {xy}) - ({x} *{y}))/(({n} *{xx}) - {x**2})")
    print(f"({n} * {xy}) - ({x} *{y}))/(({n} *{xx}) - {x**2})")
    print(f"({n} * {xy}) - ({x} *{y}))/(({n *xx}) - {x**2})")
    print(f"({n * xy}) - ({x *y}))/({(n *xx) - x**2})")
    return ((n * xy) - (x *y))/((n *xx) - x**2)

coef_ang = f_coef_ang()

def f_coef_lin():
    return (y - coef_ang * x)/n

coef_lin = f_coef_lin()

def f(x):
    return coef_lin + coef_ang * x

