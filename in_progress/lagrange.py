import pandas as pd
from sympy import symbols, simplify

# Define the given data
x_lst = [2, 8, 10, 15]
y_lst = [5, 10, 15,20]
#y_lst = [v * 10 **3 for v in x_lst]

my_x = 6.08
target = my_x

data = {
    "x": x_lst,
    "y": y_lst
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Determine the degree of the Lagrange interpolation
degree = len(df) - 1

# Define the target value for interpolation

# Define the symbols and variables
x = symbols('x')
y = symbols('y')

# Define the Lagrange interpolation formula
interpolation = 0
L_values = []

for i in range(degree + 1):
    term = 1
    for j in range(degree + 1):
        if i != j:
            term *= (x - df['x'][j]) / (df['x'][i] - df['x'][j])
    interpolation += term * df['y'][i]
    L_values.append(term)

# Substitute the target value into the interpolation formula
interpolated_value = interpolation.subs(x, target)

# Simplify the interpolated value
simplified_value = simplify(interpolated_value)


# Print the results
print("Given Data:")
print(df)
print()
print("Lagrange Interpolation:")
print(f"For x = {target}, y = {simplified_value}")
print()


