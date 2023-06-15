import math as mt
import pandas as pd
from bisection_func import *
from bolzano_func import bolzano

# Define an empty list to store all the DataFrames
dfs = []

#EX2-AP1

print("-----------------------------------------------")
print("A:")
f = lambda x: 3**x -5*x-10
a = 2
b = 3
tol = .2
df = find_root_bisection(f, a, b, tol)
