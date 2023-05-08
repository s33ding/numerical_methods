import numpy as np

# Create a 5x3 matrix of random integers between 0 and 9
# The integers are generated between 0 and 9 using the numpy.random.randint() function
matrix = np.random.randint(0, 10, size=(5, 3))


print("Original matrix:")
print(matrix)


# Obtain the upper triangular matrix using NumPy's triu() function
"""
In the context of Gaussian elimination, the upper triangle refers to the matrix that is obtained after performing a sequence of elementary row operations on an augmented matrix to transform it into row echelon form.

The upper triangle matrix has zeros below the main diagonal, which is the diagonal that runs from the upper left corner of the matrix to the lower right corner. The entries above the main diagonal may be nonzero, but they are called the upper triangular part of the matrix.

The upper triangular form is useful in solving linear systems of equations, as it allows for a simpler process of back substitution to find the solution. Specifically, the solution can be obtained by solving for the variable associated with the last row of the upper triangle, then substituting that value into the second-to-last row, and so on until all variables have been solved for.

In summary, the upper triangle in Gaussian elimination refers to the matrix that is obtained after applying elementary row operations to an augmented matrix to put it in row echelon form, and it is useful for solving systems of linear equations.
"""

upper_triangular = np.triu(matrix)

# Print the upper triangular matrix
print("Upper triangular matrix:")
print(upper_triangular)


"""
The next step depends on the specific goal of the problem. Here, the code has already obtained the upper triangular matrix using NumPy's triu() function, so the next step could be any further processing or analysis needed based on this matrix.

For example, if the goal is to solve a system of linear equations using Gaussian elimination, the next step would be to perform back substitution on the upper triangular matrix to obtain the solution. If the goal is to compute the determinant of the matrix, the upper triangular form can be used to simplify the computation.

Alternatively, if the goal is to perform additional transformations on the matrix using Gaussian elimination, the code could continue with the row operations to further reduce the matrix to reduced row echelon form.
"""
