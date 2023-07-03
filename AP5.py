import sympy as sp
import pandas as pd
import numpy as np
from shared_func.newton_interpolation_func import * 

# ex1
x_specific = 12  
x, y = "x","f(x)"
data = {
    x:list(range(5,16,5)),
    y:[49, 105, 172]
}

df = pd.DataFrame(data)
ex1_df, ex1_d_df, ex1_polynomial_print_1, ex1_polynomial_print_2, ex1_result_print= big_process(df, x, y, x_specific)

# ex2
x_specific = 0
x, y = "x","f(x)"
data = {
    x:[1, -1, -2],
    y:[0, -3, -4]
}

df = pd.DataFrame(data)
ex2_df, ex2_d_df, ex2_polynomial_print_1, ex2_polynomial_print_2, ex2_result_print= big_process(df, x, y, x_specific)


# ex3
x_specific = 0.5
x, y = "x","f(x)"
data = {
    x:[-2, -1, 1, 2],
    y:[0, 1, -1, 0]
}

df = pd.DataFrame(data)
ex3_df, ex3_d_df, ex3_polynomial_print_1, ex3_polynomial_print_2, ex3_result_print= big_process(df, x, y, x_specific)

# ex4
x_specific = 0.5
x, y = "x","f(x)"
data = {
    x:[1, 3 ,5 ,7 , 20],
    y:[800, 2310, 3090, 3940, 8000]
}

df = pd.DataFrame(data)
ex4_df, ex4_d_df, ex4_polynomial_print_1, ex4_polynomial_print_2, ex4_result_print= big_process(df, x, y, x_specific)

# ex5
x_specific = 2.5
x, y = "x","f(x)"
data = {
    x:[1.5, 2.0, 3.5],
    y:[2.5, 3.1, 7.0]
}

df = pd.DataFrame(data)
ex5_df, ex5_d_df, ex5_polynomial_print_1, ex5_polynomial_print_2, ex5_result_print= big_process(df, x, y, x_specific)

with open('media/style.css', 'r') as f:
    css = f.read()

# Write HTML file
with open('media/ap5-ex1.html', 'w') as f:
    f.write('<html>\n<head>\n')
    f.write(f'<style>\n{css}\n</style>\n')
    title = "AP5"
    f.write('</head>\n<body>\n')
    f.write(f'<h1>{title}</h1>\n')

    title = "EX:1"
    poly_1 = ex1_polynomial_print_1
    poly_2 = ex1_polynomial_print_2
    res = ex1_result_print
    df = ex1_df
    d_df = ex1_d_df

    f.write(f"<h4>{title}</h4>")
    f.write(df.to_html(index=False))
    f.write(d_df.to_html(index=False))
    f.write(f"<p>{poly_1}</p>")
    f.write(f"<p>{poly_2}</p>")
    f.write(f"<p>{res}</p>")

    title = "EX:2"
    poly_1 = ex2_polynomial_print_1
    poly_2 = ex2_polynomial_print_2
    res = ex2_result_print
    df = ex2_df
    d_df = ex2_d_df

    f.write(f"<h4>{title}</h4>")
    f.write(df.to_html(index=False))
    f.write(d_df.to_html(index=False))
    f.write(f"<p>{poly_1}</p>")
    f.write(f"<p>{poly_2}</p>")
    f.write(f"<p>{res}</p>")

    title = "EX:3"
    poly_1 = ex3_polynomial_print_1
    poly_2 = ex3_polynomial_print_2
    res = ex3_result_print
    df = ex3_df
    d_df = ex3_d_df

    f.write(f"<h4>{title}</h4>")
    f.write(df.to_html(index=False))
    f.write(d_df.to_html(index=False))
    f.write(f"<p>{poly_1}</p>")
    f.write(f"<p>{poly_2}</p>")
    f.write(f"<p>{res}</p>")

    title = "EX:4"
    poly_1 = ex4_polynomial_print_1
    poly_2 = ex4_polynomial_print_2
    df = ex4_df
    d_df = ex4_d_df
    res = f"D3 = {d_df['D3'].iloc[0]}; D4 = {d_df['D4'].iloc[0]}"

    f.write(f"<h4>{title}</h4>")
    f.write(df.to_html(index=False))
    f.write(d_df.to_html(index=False))
    f.write(f"<p>{res}</p>")

    title = "EX:5"
    poly_1 = ex5_polynomial_print_1
    poly_2 = ex5_polynomial_print_2
    res = ex5_result_print
    df = ex5_df
    d_df = ex5_d_df

    f.write(f"<h4>{title}</h4>")
    f.write(df.to_html(index=False))
    f.write(d_df.to_html(index=False))
    f.write(f"<p>{poly_1}</p>")
    f.write(f"<p>{poly_2}</p>")
    f.write(f"<p>{res}</p>")

