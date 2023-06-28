import math as mt
import pandas as pd

#data =  {
#            'x':[14,6,3,6,7,6,7,4,8,7,6,4],
#            'y':[10,26,41,29,27,27,19,28,19,31,29,33]
#        }
#data = {
#        "x":[1,2,3,4,5,6],
#        "y":[80.5,81.6,82.1,83.7,83.9,85]
#        }

data = {
        "x":[x for x in range(5,40,5)],
        "y":[7,8.4,9.6,10.5,11.9,11.3,12]
        }

df = pd.DataFrame(data)
df['xy'] = df.x * df.y
df['xx'] = df.x **2


sum_x= df["x"].sum()
sum_y = df["y"].sum()
sum_xy =df["xy"].sum()
sum_xx=df["xx"].sum()

total = {
    "sum_x":sum_x,
    "sum_y":sum_y,
    "sum_xy":sum_xy,
    "sum_xx":sum_xx
}

df2 = pd.DataFrame(total, index=[0])
print(df2)
n = len(df)
def f_coef_ang():
    print(f"======================================================")
    print(f"f_coef_ang:")
    print(f"(n * sum_xy) - (sum_x * sum_y))/((n * sum_xx) - sum_x**2))")
    print(f"({n} * {sum_xy}) - ({sum_x} * {sum_y}))/(({n} * {sum_xx}) - {sum_x**2}))")
    print(f"({(n * sum_xy) - (sum_x * sum_y)})/({n * sum_xx - sum_x**2})")
    print(f"======================================================")
    return ((n * sum_xy) - (sum_x * sum_y))/((n * sum_xx) - sum_x**2)

#a
a = f_coef_ang()

def f_coef_lin():
    print(f"======================================================")
    print(f"f_coef_ling:")
    print(f"(sum_y - a * sum_x)/n")
    print(f"({sum_y} - {a} * {sum_x})/{n}")
    print(f"======================================================")
    return (sum_y - a * sum_x)/n

#b
b = f_coef_lin()

def f(x):

    print(f"y = ax + b")
    print(f"y = coef_ang * x + coef_lin")
    print(f"y = {a} * {x} + {b}")
    return a*x + b

print(df)
x=int(input("x:"))
print("a:",a)
print("b:",b)
print("x:",x)

y=f(x)
print("y:",y)
