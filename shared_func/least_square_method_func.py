import pandas as pd

def compute_totals(df):
    print("===============================================")
    print("df:")
    print(df)
    df["xy"] = df.x * df.y
    df["xx"] = df.x * df.x

    total_x = df["x"].sum()
    total_y = df["y"].sum()
    total_xy = df["xy"].sum()
    total_xx = df["xx"].sum()

    n = len(df)

    data = {
        "total_x": [total_x],
        "total_y": [total_y],
        "total_xy": [total_xy],
        "total_xx": [total_xx],
        "n": [n]
    }

    df_total = pd.DataFrame(data)
    print("===============================================")
    print("df_total:")
    print(df_total)

    return n, total_x, total_y, total_xy, total_xx, df_total
    
def f_a(n, total_x, total_y, total_xy, total_xx):
    print("===============================================")
    formula = "((n*total_xy) - (total_x*total_y))/((n*total_xx) - (total_x**2))"
    a = ((n*total_xy) - (total_x*total_y))/((n*total_xx) - (total_x**2))
    a = round(a, 3)

    print_fa_1 = f"a = {formula}"
    print_fa_2 = f"a = {(n*total_xy) - (total_x*total_y)}/{(n*total_xx) - (total_x**2)}"
    print_fa_3 = f"a = {a}\n"

    print(print_fa_1)
    print(print_fa_2)
    print(print_fa_3)
    return a, print_fa_1, print_fa_2, print_fa_3 

def f_b(n, total_x, total_y, a):
    print("===============================================")
    formula = "(total_y - (total_x * a)) / n"
    b = (total_y - (total_x * a)) / n
    b = round(b,3)

    print_fb_1 = f"b = {formula}"
    print_fb_2 = f"({total_y} - ({total_x} * {a})) / {n}"
    print_fb_3 = f"b = {b}\n"
    print(print_fb_1)
    print(print_fb_2)
    print(print_fb_3)
    return b, print_fb_1, print_fb_2, print_fb_3 

def f(x, a, b):
    print("===============================================")
    y =  a * x + b
    print_f1 = "y = a * x - b"
    print_f2 = f"f(x) = {a} * x + {b}"
    print_f3 = f"f({x}) = {a} * {x} + {b} = {y}"

    print(print_f1)
    print(print_f2)
    print(print_f3)
    print(f"y = {y}")

    return y, print_f1, print_f2, print_f3

def big_process(df, x_specific):
    n, total_x, total_y, total_xy, total_xx, df_total = compute_totals(df)
    a, *print_fa = f_a(n, total_x, total_y, total_xy, total_xx)

    coef_ang  = a
    a2 = a 

    b, *print_fb = f_b(n, total_x, total_y, a)

    coef_lin = b
    a1 = b

    x = x_specific
    y, *print_f = f(x, a, b)
    data = {'y': [y], 'x': [x], 'a': [a], 'b': [b]}
    df_summary = pd.DataFrame(data)
    print("===============================================")
    print("df_summary:")
    print(df_summary)
    return df_total, df_summary, print_fa, print_fb, print_f
