import random

def percolate():
  global matrix
  stop, count = False, 0
  while not stop:
    indexToFill = openBlocks()
    count += 1
    if isNeighbourFilled(matrix, indexToFill[0], indexToFill[1]):
      fill(matrix, indexToFill[0], indexToFill[1])
    if isFilled(matrix):
      stop = True
  return count/(len(matrix) * len(matrix))

def isNeighbourFilled(matrix, i, j):
  n = len(matrix)
  # if matrix[i + 1][j] == 2 or matrix[i - 1][j] == 2 or matrix[i][j + 1] == 0 or matrix[i][j - 1] == 0:
  #   return True
  if i + 1 < n:
    if matrix[i + 1][j] == 2:
      return True
  if i - 1 >= 0:
    if matrix[i - 1][j] == 2:
      return True
  if j + 1 < n:
    if matrix[i][j + 1] == 2:
      return True
  if j - 1 > 0:
    if matrix[i][j - 1] == 2:
      return True
  return False

def startFilling():
  global matrix
  for j in range(0, len(matrix)):
    if matrix[0][j] == 0:
      return True
  return False 

def openBlocks():
  global blocks
  global matrix
  indexToOpen = random.randrange(0, len(blocks))
  matrix[blocks[indexToOpen][0]][blocks[indexToOpen][1]] = 0
  indexToFill = [blocks[indexToOpen][0], blocks[indexToOpen][1]]
  # if indexToFill[0] == 0:
  #   fill(matrix, indexToFill[0], indexToFill[1])
  blocks.pop(indexToOpen)
  displayMatrix(matrix)
  return indexToFill

def isFilled(matrix):
    for i in range(0, len(matrix)):
        if matrix[n - 1][i] == 2:
            return True

def displayMatrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            print(matrix[i][j], end = ' ')
        print(' ')
    print(' ')

def fill(matrix, i, j):
    """
    1 means filled with block
    0 means vacant
    2 means filled with water
    """
    # print(i, j)
    if matrix[i][j] == 0:
        matrix[i][j] = 2
        # displayMatrix(matrix)
        if (i >= 0 and i < n) and (j >= 0 and j < n):
            if j - 1 >= 0:
                fill(matrix, i, j - 1)
            if j + 1 < n:
                fill(matrix, i, j + 1)
            if i + 1 < n:
                fill(matrix, i + 1, j)
            if i - 1 >= 0:
                fill(matrix, i - 1, j)
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

#main 
result = []
n = int(input("enter the size of the matrix!"))
for i in range(0, 200):
  matrix = []
  blocks = []
  # n = int(input("enter the size of the matrix!"))
  for i in range(0, n):
    for j in range(0, n):
      blocks.append([i, j])
  for i in range(0, n):
      matrix.append([])
  for i in range(0, n):
      for j in range(0, n):
          matrix[i].append(1)
  displayMatrix(matrix)

  while True:
    index = openBlocks()
    if startFilling():
      fill(matrix, index[0], index[1])
      break
  result.append(percolate())
print(sum(result) / (len(result)))

# for j in range(0, n):
#     if matrix[0][j] == 0:
#         fill(matrix, 0, j)
print("\n\n\n*****************************FINAL OUTPUT************************")
displayMatrix(matrix)
