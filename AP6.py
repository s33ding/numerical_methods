import sympy as sp
import pandas as pd
import numpy as np
from shared_func.least_square_method_func import * 

# ex1
print("EX1:")
x_specific = 8  
x, y = "x","y"
data = {
    x:list(range(1,7)),
    y:[80.5, 81.6, 82.1, 83.7,83.9, 85]
}
df = pd.DataFrame(data)
ex1_df = df 
ex1_df_total, ex1_df_summary, ex1_print_fa, ex1_print_fb, ex1_print_f = big_process(df, x_specific)


# ex2
print("EX2:")
x_specific = 18  
x, y = "x","y"
data = {
    "cidade":"A B C D E F G H".split(),
    x:[5, 10 , 20 , 8, 4, 6, 12, 15],
    y:[27, 46, 73, 40, 30, 28, 46, 59]
}
df = pd.DataFrame(data)
ex2_df = df 
ex2_df_total, ex2_df_summary, ex2_print_fa, ex2_print_fb, ex2_print_f = big_process(df, x_specific)

# ex3
print("EX3:")
x_specific = 20  
x, y = "x","y"
data = {
    x:list(range(10,16)),
    y:[100, 112, 119, 130, 139, 142]
}
df = pd.DataFrame(data)
ex3_df = df 
ex3_df_total, ex3_df_summary, ex3_print_fa, ex3_print_fb, ex3_print_f = big_process(df, x_specific)
# Write HTML file
title = "AP6"

with open('media/style.css', 'r') as f:
    css = f.read()

with open(f'media/{title}.html', 'w') as f:
    f.write('<html>\n<head>\n')
    f.write(f'<style>\n{css}\n</style>\n')
    f.write('</head>\n<body>\n')
    f.write(f'<h1>{title}</h1>\n')

    title = "EX:1"
    f.write(f'<h1>{title}</h1>\n')
    f.write(ex1_df.to_html(index=False))
    f.write(ex1_df_total.to_html(index=False))
    f.write(ex1_df_summary.to_html(index=False))
    f.write(f'<br>')
    for val in ex1_print_fa:
        f.write(f'<p1>{val}</p1><br>')
    f.write(f'<br>')
    for val in ex1_print_fb:
        f.write(f'<p1>{val}</p1><br>')
    f.write(f'<br>')
    
    f.write(f'<p3><b>A:</b></p3><br>')
    for val in ex1_print_f[:2]:
        f.write(f'<p1>{val}</p1><br>')
    f.write(f'<br>')
    f.write(f'<p3><b>B:</b></p3><br>')
    for val in ex1_print_f[:2]:
        f.write(f'<p1>{val}</p1><br>')
    f.write(f'<br>')
    f.write(f'<p3><b>C:</b></p3><br>')

    x = 12200
    df_summary = ex1_df_summary
    a = df_summary.a.iloc[0]
    b = df_summary.b.iloc[0]
    y = 85 

    txt = f"y = {y}"
    f.write(f'<p1>{txt}</p1><br>')
    txt = f"x = {a} * {y} + {b}"
    f.write(f'<p1>{txt}</p1><br>')
    x = (y - b)/a
    res = x
    txt = f"x = {res}; answer: {round(x,3)}%"
    f.write(f'<p1>{txt}</p1><br>')

    title = "EX:2"
    f.write(f'<h1>{title}</h1>\n')
    f.write(ex2_df.to_html(index=False))
    f.write(ex2_df_total.to_html(index=False))
    f.write(ex2_df_summary.to_html(index=False))
    f.write(f'<br>')
    for val in ex2_print_fa:
        f.write(f'<p1>{val}</p1><br>')
    f.write(f'<br>')
    for val in ex2_print_fb:
        f.write(f'<p1>{val}</p1><br>')
    f.write(f'<br>')
    
    f.write(f'<p3><b>A:</b></p3><br>')
    for val in ex2_print_f[:2]:
        f.write(f'<p1>{val}</p1><br>')
    f.write(f'<br>')
    f.write(f'<p3><b>B:</b></p3><br>')
    for val in ex2_print_f[:2]:
        f.write(f'<p1>{val}</p1><br>')
    f.write(f'<br>')
    f.write(f'<p3><b>C:</b></p3><br>')

    x = 18
    df_summary = ex2_df_summary
    a = df_summary.a.iloc[0]
    b = df_summary.b.iloc[0]
    y = 50 
    txt = f"y = {y}"
    f.write(f'<p1>{txt}</p1><br>')
    txt = f"x = {a} * {y} + {b}"
    f.write(f'<p1>{txt}</p1><br>')

    x = (y - b)/a
    res = x
    txt = f"x = {res}; answer: R${x* 1000}"
    f.write(f'<p1>{txt}</p1><br>')

    title = "EX:3"
    f.write(f'<h1>{title}</h1>\n')
    f.write(ex3_df.to_html(index=False))
    f.write(ex3_df_total.to_html(index=False))
    f.write(ex3_df_summary.to_html(index=False))
    f.write(f'<br>')
    for val in ex3_print_fa:
        f.write(f'<p1>{val}</p1><br>')
    f.write(f'<br>')
    for val in ex3_print_fb:
        f.write(f'<p1>{val}</p1><br>')
    f.write(f'<br>')
    
    f.write(f'<p3><b>A:</b></p3><br>')
    for val in ex3_print_f:
        f.write(f'<p1>{val}</p1><br>')
    f.write(f'<br>')

    f.write(f'<p3><b>B:</b></p3><br>')
    df_summary = ex3_df_summary
    x = df_summary['x'].iloc[0]
    a = df_summary['a'].iloc[0]
    b = df_summary['b'].iloc[0]
    txt = f"x = {x}"
    f.write(f'<p1>{txt}</p1><br>')
    y = a * x + b
    txt = f"f({x}) = {a} * {x} + {b}"
    f.write(f'<p1>{txt}</p1><br>')
    txt = f"answer: R${y*1000}"
    f.write(f'<p1>{txt}</p1><br>')


    f.write(f'<br>')
    f.write(f'<p3><b>C:</b></p3><br>')

    df_summary = ex3_df_summary
    x = df_summary['x'].iloc[0]
    a = df_summary['a'].iloc[0]
    b = df_summary['b'].iloc[0]
    y = 160 
    txt = f"y = {y}"
    f.write(f'<p1>{txt}</p1><br>')
    txt = f"x = {a} * {y} + {b} = {x}; answer:R${x* 1000}"
    f.write(f'<p1>{txt}</p1><br>')

    x = (y - b)/a
    res = x
    txt = f"x = {res} "
    f.write(f'<p1>{txt}</p1><br>')
