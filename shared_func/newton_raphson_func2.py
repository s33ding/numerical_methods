import pandas as pd

def newton_raphson(f, f_diff, x_val, iter_count, max_iter, tol):
    f_val = f(x_val)
    f_diff_val = f_diff(x_val)
    x_new = x_val - f_val / f_diff_val

    data = {'Iteration': [iter_count],
            'x': [x_val],
            'f(x)': [f_val],
            "f'(x)": [f_diff_val],
            'x_new': [x_new],
            '|x_new - x|': [abs(x_new - x_val)]}
    df = pd.DataFrame(data)
    if abs(x_new - x_val) < tol or iter_count >= max_iter:
        return df, x_new
    else:
        recursive_df, solution = newton_raphson(f, f_diff, x_new, iter_count + 1, max_iter, tol)
        return pd.concat([df, recursive_df]), solution
