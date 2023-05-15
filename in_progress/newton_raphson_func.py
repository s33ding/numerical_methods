import math as mt 
import sympy as sp 

def newton_raphson_cal(f,x,fx=None):

    if fx is None:
        fx = f(x)

    x = symbols('x')
    df_dx = f(x).diff(x)
    res = x - (fx/df_dx)
    rw = {"x":x,"fx":fx,"df_dx":df_dx,"res":res}
    print(rw)
    print(f"""
    {round(r,4)} = {round(x,4)} - {round(fx,4)}/{round(d)}
    """)
    return rw

def nr_stop_criterion(res,tol):
    return res <= tol

def newton_rathson(f,x, tol, matrix = [], fx=None):
    rw = newton_raphson_cal(f,x)
    res = rw.get("res")
    stop = nr_stop_criterion(res,tol)
    matrix.append(rw) 
    if stop == True:
        return matrix
    else:
        x = rw.get("x")
        fx = rw.get("fx")
        return newton_rathson( f, x, tol, matrix, fx)
