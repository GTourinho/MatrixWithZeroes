# Author: Gabriel Tourinho Badaró
# Um algoritmo para que se um elemento em uma matriz MxN é 0, todos os elementos da linha e coluna deste elemento recebam também o valor 0.
# An algorithm that inputs the value 0 for all elements of rows and columns with at least an element of value 0

#Helper functions
def getmatrix():
  matrix = []
  nRows = 1
  row = [int(n) for n in input().split()]
  nColumns = len(row)
  matrix.append(row)
  while nColumns > 0:
    row = [int(n) for n in input().split()]
    if row == []:
      break
    if len(row) != nColumns:
      exit("Error: different row lengths")
    matrix.append(row)
    nRows+=1
  return matrix, nRows, nColumns

#Get Matrix
print('Insert matrix lines (blank line to end):')
matrix, nRows, nColumns = getmatrix()
if matrix == [[]]:
  exit('Error: empty matrix')

#Helper hashes
intactRows = {}
foundZeroColumns = {}

#Draw Rows, find Columns with zeroes and Intact Rows
for row in range(nRows):
  draw = False
  for column in range(nColumns):
    if matrix[row][column] == 0:
      draw = True
      foundZeroColumns[column] = 1
  if draw:
    matrix[row] = [0]*nColumns
  else:
    intactRows [row] = 1

#Draw Columns
for column in foundZeroColumns:
  for row in intactRows:
    matrix[row][column] = 0

#Print result
print('Result matrix:')
for row in matrix:
  for column in range(nColumns):
    print(row[column], end = '')
    print(' ', end = '')
  print('')