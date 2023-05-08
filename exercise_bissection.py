import math as mt
import pandas as pd
from bisection_func import *
from bolzano_func import bolzano

# Define an empty list to store all the DataFrames
dfs = []

#EX2-AP1

print("-----------------------------------------------")
print("A:")
f = lambda x: mt.e **x + x
a = -1
b = 1
tol = .26
df = find_root_bisection(f, a, b, tol)
if df is not None:
    # If a DataFrame is returned, append it to the list with a title
    dfs.append(('A', df))

print("-----------------------------------------------")
print("B:")
f = lambda x: mt.e **-x + x**2 - 2
a = -1
b = 1
tol = .15
df = find_root_bisection(f, a, b, tol)
if df is not None:
    # If a DataFrame is returned, append it to the list with a title
    dfs.append(('B', df))

print("-----------------------------------------------")
print("C:")
f = lambda x: x**2 - 3
a = 1
b = 2
tol = .1
df = find_root_bisection(f, a, b, tol)
if df is not None:
    # If a DataFrame is returned, append it to the list with a title
    dfs.append(('C', df))

print("-----------------------------------------------")
print("D:")
f = lambda x:x**3-7
a = 1.5
b = 2.5
tol = .15
df = find_root_bisection(f, a, b, tol)
if df is not None:
    # If a DataFrame is returned, append it to the list with a title
    dfs.append(('D', df))

print("-----------------------------------------------")
print("E:")
f = lambda x:x**2 + mt.log(x)
a = .5
b = 1
tol = .035
df = find_root_bisection(f, a, b, tol)
if df is not None:
    # If a DataFrame is returned, append it to the list with a title
    dfs.append(('E', df))

# Concatenate all the DataFrames into a single DataFrame
all_dfs = pd.concat([df[1] for df in dfs])

# Read CSS file
with open('media/style.css', 'r') as f:
    css = f.read()

# Write HTML file
with open('media/ap1-ex2.html', 'w') as f:
    f.write('<html>\n<head>\n')
    f.write(f'<style>\n{css}\n</style>\n')
    f.write('</head>\n<body>\n')
    f.write('<h1>Exercise 2</h1>\n')
    for title, df in dfs:
        f.write(f"<h4>{title}</h4>")
        a = df["a"].iloc[-1]
        b = df["b"].iloc[-1]
        res = (a+b)/2
        f.write(f"<p>X = {res}</p>")
        f.write(df.to_html(index=False))
    f.write('</body>\n</html>\n')

