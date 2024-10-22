
import numpy as np

def normalizeAdjacencyMatrix(A):
    n = len(A)
    A = np.array(A, dtype=float)  # Ensure A is a NumPy array of floats
    for j in range(A.shape[1]):  # Iterate over each column
        sumOfCol = np.sum(A[:, j])  # Sum of the column
        if sumOfCol == 0:
            A[:, j] = 1 / n  # Handling dangling nodes
        else:
            A[:, j] /= sumOfCol  # Normalize the column
    return A

def dampingMatrix(A, d=0.85):
    n = len(A)
    Q = np.ones((n, n), dtype=float) / n  # Create a matrix of size n with all values as 1/n
    arrA = np.array(A, dtype=float)
    arrM = d * arrA + (1 - d) * Q  # Apply damping factor
    return arrM

def findSteadyState(M, n):
    eigenvalues, eigenvectors = np.linalg.eig(M)  # Calculate eigenvalues and eigenvectors
    idxWithEval1 = np.argmax(np.isclose(eigenvalues, 1))  # Find index of eigenvalue close to 1
    steadyStateVector = eigenvectors[:, idxWithEval1].real  # Get the corresponding eigenvector
    steadyStateVector /= np.sum(steadyStateVector)  # Normalize to sum to 1
    return steadyStateVector

def pageRank(A, d=0.85):
    n = len(A)
    A = normalizeAdjacencyMatrix(A)  # Normalize the adjacency matrix
    M = dampingMatrix(A, d)  # Create the damping matrix
    steadyStateVectorOfA = findSteadyState(M, n)  # Find the steady state vector
    return steadyStateVectorOfA

# Testing the PageRank function
print("\nPage Rank Examples")
matrix1 = [
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]
print("1) Matrix 1 =", matrix1)
print("Steady State Vector:", pageRank(matrix1))

matrix2 = [
    [0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0]
]
print("\n2) Matrix 2 =", matrix2)
print("Steady State Vector:", pageRank(matrix2))
