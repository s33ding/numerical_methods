import math as mt
import pandas as pd
from numpy import log as ln

#"transform the exp. func. to make it linear and use the linear regression"

#lst_x = [-1,-.7, -.4,-.1,.2,.5, .8, 1 ]
lst_x = [int(x) for x in "0 1 2 3 4 5".split()]
#lst_y = [36.547,17.264, 8.155,3.852,1.82, .86, .406,.246]
lst_y = [int(x) for x in "8389 6540 5000 3200 2500 2000".split()]

data = {'x':lst_x, 'y':lst_y}

df = pd.DataFrame(data)

df['z'] = df.y.apply(lambda a: mt.log(a,mt.e))
df['xz'] = df.x * df.z
df['xx'] = df.x * df.x

sum_x = df.x.sum()
sum_z = df.z.sum()
sum_xz = df.xz.sum()
sum_xx = df.xx.sum()
n = len(df)
def f_a2():
    print(f"({(n*sum_xz) -(sum_x*sum_z)}/({(n*sum_xx) - (sum_x**2)})")
    return ((n*sum_xz) - (sum_x*sum_z))/((n*sum_xx) - (sum_x**2)) 

def f_a1():
    return ((sum_z - a2 * sum_x))/n


a2 = f_a2()
a1 = f_a1()

alfa_1 = mt.e ** a1
alfa_2 = -1 * a2

def f(x):
    print(alfa_1*(mt.e**alfa_2))
    return alfa_1*(mt.e**alfa_2)

f(180)
