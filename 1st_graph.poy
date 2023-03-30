import numpy as np
import matplotlib.pyplot as plt

# Define your function here
def f(x):
    return (x**3) - (9*x) + 3

# Define the bisection method to find roots
def bisection(f, a, b, tol):
    fa, fb = f(a), f(b)
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        fc = f(c)
        if fc == 0:
            return c
        elif np.sign(fc) == np.sign(fa):
            a, fa = c, fc
        else:
            b, fb = c, fc
    return (a + b) / 2

# Create a range of x values to plot
x = np.linspace(-5, 5, 1000)

# Plot the function
plt.plot(x, f(x))

# Use bisection method to find roots
root1 = bisection(f, -5, 0, 1e-6)
root2 = bisection(f, 0, 5, 1e-6)

# Plot the roots as vertical lines
plt.axvline(x=root1, color='r')
plt.axvline(x=root2, color='r')

# Add x and y axis labels
plt.xlabel('x')
plt.ylabel('f(x)')

# Add a title to the plot
plt.title('Graph of f(x) with roots')

# Show the plot
plt.show()

