import math as mt 
import sympy as sp 

def newton_raphson_cal(f,x):
    fx = f(x)
    x = symbols('x')
    d = f(x).diff(x))
    r = x - (fx/d)
    print(f"""
    {round(r,4)} = {round(x,4)} - {round(fx,4)}/{round(d)}
    """)
    return r, d

def nr_stop_criterion(r,tol):
    return r < tol

def newton_rathson(f,x, tol, matrix = [], ):
    r,d = newton_raphson_cal(f,x)
    
