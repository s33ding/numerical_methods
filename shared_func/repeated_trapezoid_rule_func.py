import math as mt
import sympy as  sp


def make_derivative_lambda(lambda_func):
    x = sp.symbols('x')
    f_expr = lambda_func(x)
    f_diff_expr = sp.diff(f_expr, x)
    f_diff = sp.lambdify(x, f_diff_expr)
    show_expression(msg="f'(x)", expression=f_diff_expr)
    return f_diff

def calculate_max_second_derivative(f_II, a, b):
    f_II_a = f_II(a)
    f_II_b = f_II(b)
    f_II_max = max(f_II_a, f_II_b)
    return f_II_max,f_II_b,f_II_a 

def trapezoidal_rule(f, n, a, b):
    f_I = make_derivative_lambda(f)
    f_II = make_derivative_lambda(f_I)
    f_II_max, f_II_b, f_II_a  = calculate_max_second_derivative(f_II, a, b)
    h = (b-a)/n
    res_erro = (((b-a)*(h**2))/12) * f_II_max

    s = (f(a) + f(b))
    for i in range(1, n):
        s += 2 * f(a + i * h)
    
    res_integral = (h / 2) * s
    n_print = f"n = {n}"
    a_print = f"a = {a}"
    b_print = f"b = {b}"
    h_print_1= f"h = ( b - a ) / n = ( {b} - {a} ) / {n} "
    h_print_2= f"h = {h}"
    h = (b-a)/n
    f_II_a_print = f"f''(a) = f({a}) = {f_II_a}"
    f_II_b_print = f"f''(b) = f({b}) = {f_II_b}"
    f_print = f"MAX |f''(x)| = {f_II_max}"
    print_erro_1 = f"erro = (((b-a)*(h**2))/12) * MAX |f''(x)|"
    print_erro_2 = f"erro = ((({b}-{a})*({h}**2))/12) * {f_II_max}"
    print_erro_3 = f"erro = {res_erro}"
    print_final_result = f"result = {res_integral*res_erro}"

    result_str = [n_print, a_print, b_print, h_print_1, h_print_2,  f_II_a_print, f_II_b_print, f_print, print_erro_1, print_erro_2, print_erro_3, print_final_result ]
    for val in result_str :
        print(val)
    return result_str

def show_expression(msg, expression):
    print(f"{msg}:")
    res = sp.pretty(expression, use_unicode=True)
    print(res)
    print("--------")

