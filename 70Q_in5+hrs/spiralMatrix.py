def spiralTraversal(matrix):
  ret = []
  while matrix:
    # step1
    ret += (matrix.pop(0))

    # Step 2
    if matrix and matrix[0]:
      for row in matrix:
        ret.append(row.pop())
    
    # Step 3
    if matrix:
      ret += (matrix.pop()[::-1])

    # Step 4
    if matrix and matrix[0]:
      for row in matrix[::-1]:
        ret.append(row.pop(0))
  return ret



