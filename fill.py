import random

# def populateMatrix(n):

def ifFilled(matrix):
    for i in range(0, len(matrix)):
        if matrix[n - 1][i] == 2:
            return True

def displayMatrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            print(matrix[i][j], end = '')
        print(' ')
    print(' ')

def fill(matrix, i, j):
    print(i, j)
    if matrix[i][j] == 0:
        matrix[i][j] = 2
        displayMatrix(matrix)
        if (i >= 0 and i < n) and (j >= 0 and j < n):
            if j - 1 >= 0:
                fill(matrix, i, j - 1)
            if j + 1 < n:
                fill(matrix, i, j + 1)
            if i + 1 < n:
                fill(matrix, i + 1, j)
            if i - 1 >= 0:
                fill(matrix, i - 1, j)
    else:
        print(' ')
    return

# main script demo
# matrix = []
# n = int(input("enter the size of the matrix!"))
# for i in range(0, n):
#     matrix.append([])
# for i in range(0, n):
#     for j in range(0, n):
#         matrix[i].append(random.randint(0,1))
# displayMatrix(matrix)
# for j in range(0, n):
#     if matrix[0][j] == 0:
#         fill(matrix, 0, j)
# print("\n\n\n*****************************FINAL OUTPUT************************")
# displayMatrix(matrix)

#main script
matrix = []
n = int(input("enter the size of the matrix!"))
for i in range(0, n):
    matrix.append([])
for i in range(0, n):
    for j in range(0, n):
        matrix[i].append(1)
displayMatrix(matrix)
for j in range(0, n):
    if matrix[0][j] == 0:
        fill(matrix, 0, j)
print("\n\n\n*****************************FINAL OUTPUT************************")
displayMatrix(matrix)