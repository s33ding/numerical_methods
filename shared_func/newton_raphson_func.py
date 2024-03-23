import math as mt
import sympy as sp

def newton_raphson_cal(f, f_diff, x, tol, index, fx=None):
    if fx is None:
        fx = f(x)

    df_dx = f_diff(x)
    res = x - (fx / df_dx)
    debug_expression_1(x, fx, df_dx, res, index)
    stop_criterion, continue_bool_val = nr_stop_criterion(f,res, tol)
    rw =  {
        "x": x,
        "fx": fx,
        "df_dx": df_dx, 
        "res": res,
        "stop_criterion": stop_criterion,
        "continue": continue_bool_val,
        "index":index
        }
#    print(rw)
    for k,v in rw.items():
        print(k,"=",v)
    return rw

def nr_stop_criterion(f, res, tol):
    stop_criterion = f(res)
    stop_criterion = sp.Abs(stop_criterion)
    if stop_criterion <= tol:
        continue_bool_val  = False
    else:
        continue_bool_val  = True

    return stop_criterion, continue_bool_val  


def newton_rathson(f, f_diff, x, tol, matrix=[], fx=None,index=1):
    print(f"==========INDEX_{index}==========")
    rw = newton_raphson_cal(f, f_diff, x, tol,index, fx)
    matrix.append(rw)

    continue_bool_val =  rw.get("continue")

    if  continue_bool_val == False:
        return matrix

    if continue_bool_val == True:

        x = rw.get("res")
        fx = rw.get("stop_criterion")
        index = rw.get("index") + 1

        return newton_rathson(
            f=f, 
            f_diff=f_diff, 
            x=x,
            tol=tol, 
            matrix=matrix, 
            fx=fx,
            index=index
        )

def debug_expression_1(x, fx, df_dx, res, index):
    print("calculating:")
    print(f"x{index} = x - (fx / f'x)")
    print(f"x{index} = {x} - ({fx} / {df_dx})")
    print(f"x{index} = {res}")
    print("--------------------------------------")
