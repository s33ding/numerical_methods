import math
from shared_func.bolzano_func import bolzano

def func_a(x):
    return x**2 - 5*math.sin(x)

def func_b(x):
    return x**2 - 16 + math.sin(x)

def func_c(x):
    return 2*x**3 - 5

i = [-2, -1]
ii = [1, 3]
iii = [4, 5]

lst = [
    ["A",i],
    ["B",ii],
    ["C",iii]
]

html_content = "<html>\n<head>\n<title>AP1-SOLVED</title>\n</head>\n<body>\n"

html_content += "<h1>EXERCISE 1:</h1>\n"
html_content += "<h3>A)</h3>\n"

for item, values in lst:
    x1 = values[0]
    x2 = values[1]
    if bolzano(func_a, x1, x2):
        html_content += f"<p>Answer {item}: Has at least one root!</p>\n"
    else:
        html_content += f"<p>Answer {item}: Inconclusive!</p>\n"

html_content += "<h3>B)</h3>\n"
for item, values in lst:
    x1 = values[0]
    x2 = values[1]
    if bolzano(func_b, x1, x2):
        html_content += f"<p>Answer {item}: Has at least one root!</p>\n"
    else:
        html_content += f"<p>Answer {item}: Inconclusive!</p>\n"

html_content += "<h3>C)</h3>\n"
for item, values in lst:
    x1 = values[0]
    x2 = values[1]
    if bolzano(func_c, x1, x2):
        html_content += f"<p>Answer {item}: Has at least one root!</p>\n"
    else:
        html_content += f"<p>Answer {item}: Inconclusive!</p>\n"

html_content += "</body>\n</html>"

with open('media/ap1-ex1.html', 'w') as f:
    f.write(html_content)

