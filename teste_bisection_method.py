from bisection_method import *

a = 0
b = 1
tol = 1e-6

# Define function to be solved
def f(x):
    return (x**3) - (9*x) + 3

df=bisection_method(f, a=0, b=1, tol=.13)
print(df)
