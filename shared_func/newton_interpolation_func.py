import sympy as sp
import pandas as pd
import numpy as np

def calculate_divided_differences(df, x_col, y_col):
    n = len(df)
    div_diff = np.zeros((n, n))
    div_diff[:, 0] = df[y_col]

    for j in range(1, n):
        for i in range(n - j):
            div_diff[i][j] = (div_diff[i + 1][j - 1] - div_diff[i][j - 1]) / (df[x_col].iloc[i + j] - df[x_col].iloc[i])

    df_div_diff = pd.DataFrame(div_diff)
    df_div_diff = df_div_diff.rename(columns=lambda x: 'd' + str(x))
    df_div_diff = df_div_diff.replace(0, "")
    return df_div_diff

def calculate_coefficients(df_div_diff):
    coefficients = df_div_diff.iloc[0].values
    df_final = pd.DataFrame({"coefficients": coefficients})
    df_final["coefficients"] = df_final["coefficients"].apply(lambda n: round(n, 5))
    return df_final

def create_expressions(df_final, x_values):
    lst_terms = [' * '.join([f"(x - {x_values[j]})" for j in range(i)]) if i > 0 else None for i in range(len(df_final))]
    df_final['terms'] = lst_terms[1:] + ['0']

    return df_final


def create_polynomial(df_final, x_specific):
    polynomial_str = ' * '.join([f"({coef}) + {term}" for coef, term in zip(df_final['coefficients'], df_final['terms'])])
    print(f"\nThe polynomial is:\n{polynomial_str}")

    polynomial_simplified = sp.simplify(polynomial_str)
    print(f"\nThe simplified polynomial for x={x_specific} is:\n{polynomial_simplified}")


    return polynomial_str, polynomial_simplified

def big_process(df,x,y,x_specific):
    print("===============================================")
    print("df:")
    print(df)

    print("===============================================")
    # Calculate the divided differences
    df_div_diff = calculate_divided_differences(df, x, y)
    print("div_diff:")
    print(df_div_diff.iloc[0])

    print("===============================================")
    # Calculate the coefficients
    df_final = calculate_coefficients(df_div_diff)

    # Your x values for creating the terms
    x_values = df[x].values

    # Create the polynomial
    df_final = create_expressions(df_final, x_values)
    # Create the polynomial as a string
    polynomial_str, polynomial_simplified = create_polynomial(df_final, x_specific)

