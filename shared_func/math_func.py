import sympy as sp

def sp_expression(lambda_func):
    x = sp.symbols('x')
    expression = lambda_func(x)
    return expression

def sp_derivative_expression(expression):
    x = sp.symbols('x')
    derivative = sp.diff(expression, x)
    return derivative

def make_derivative_lambda(lambda_func):
    x = sp.symbols('x')
    f_expr = lambda_func(x)
    f_diff_expr = sp.diff(f_expr, x)
    f_diff = sp.lambdify(x, f_diff_expr)
    show_expression(msg="f'(x)", expression=f_diff_expr)
    return f_diff

def create_a_math_function (lambda_func):
    f_expr = sp_expression(lambda_func)
    f = lambda_func
    show_expression(msg="f", expression=f_expr)
    return f

def solve_derivative(expression, x_value):
    result = expression.subs('x', x_value)
    return result

def show_expression(msg, expression):
    print(f"{msg}:")
    res = sp.pretty(expression, use_unicode=True)
    print(res)
    print("--------")

