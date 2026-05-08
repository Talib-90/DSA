def riverSizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[j])):
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, sizes)
    return sizes

def traverseNode(i, j, matrix, visited, sizes):
    pass

matrix = [[1,0,0,1,0],
          [1,0,1,0,0],
          [0,0,1,0,1],
          [1,0,1,0,1],
          [1,0,1,1,0]]


print(visited)
