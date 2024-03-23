import pandas as pd 
from shared_func.least_square_method_func import *


# Create a DataFrame
x_specific = 100  # Replace this with your desired x value
x = "x"
lst_x = list(range(1,7))
lst_y = [80.5, 81.6, 82.1, 83.7, 83.9, 85]
y = "y"

data = {
    x: lst_x,
    y: lst_y
}

df = pd.DataFrame(data)
n, total_x, total_y, total_xy, total_xx = compute_totals(df)
print("===============================================")
print("df:")
print(df)

a = f_a(n, total_x, total_y, total_xy, total_xx)
b = f_b(n, total_x, total_y, a)
y = f(x, a ,b)
