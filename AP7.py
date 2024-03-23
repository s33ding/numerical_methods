import math as mt
from  shared_func.simpsons_func import *

#ex_1b
def f(x):
    return 5*(x**3)+(1/x)

a, b = 2, 8
n = 6

ex_13 = trapezoidal_rule(f,n, a, b)


title = "AP7"
with open('media/style.css', 'r') as f:
    css = f.read()

with open(f'media/{title}.html', 'w') as f:
    f.write('<html><head>')
    f.write(f'<style>{css}</style>')
    f.write('</head><body>')
    f.write(f'<h1>{title}</h1>')
    title = "EXERCISE 1_B:"
    f.write(f'<p8><b>{title}</b></p8><br>')
    for val in ex_1b:
        f.write(f'<p1>{val}</p1><br>')


    

