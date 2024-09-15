import numpy as np


def create_ostacules(matrix, numObstacules, a, b):
    for i in range(numObstacules):
        matrix[(np.random.randint(0, a - 1)), (np.random.randint(0, b - 1))] = 1
    return matrix


def create_posRaton(matrix, a, b):
    x = np.random.randint(0, a - 1)
    y = np.random.randint(0, b - 1)
    if matrix[x][y] == 1:
        x = np.random.randint(0, a - 1)
        y = np.random.randint(0, b - 1)
        matrix[x][y] = 2
    else:
        matrix[x][y] = 2
    return matrix


def create_posQueso(matrix, a, b):
    x = np.random.randint(0, a - 1)
    y = np.random.randint(0, b - 1)
    if matrix[x][y] == 1 or matrix[x][y] == 2:
        x = np.random.randint(0, a - 1)
        y = np.random.randint(0, b - 1)
        matrix[x][y] = 3
    else:
        matrix[x][y] = 3
    return matrix


# input matrix size matirx[a][b]
a = int(input("Enter numeber columns in matrix: "))
b = int(input("Enter number rows in matrix: "))
numObstacules = int(input("Enter number of obstacules: "))

matrix = np.zeros((a, b))
matrix = create_ostacules(matrix, numObstacules, a, b)
matrix = create_posRaton(matrix, a, b)
matrix = create_posQueso(matrix, a, b)

print(matrix)
