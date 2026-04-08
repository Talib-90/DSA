# O(N) T | O(N) S
# def spiralTraverse(array):
#     result = []
#     startingRow, endRow = 0, len(array) - 1
#     startingColumn, endCol = 0, len(array[0]) - 1
#     while startingRow <= endRow and startingColumn <= endCol:

#         for col in range(startingColumn, endCol + 1):
#             result.append(array[startingRow][col])

#         for row in range(startingRow + 1, endRow + 1):
#             result.append(array[row][endCol])

#         for col in reversed(range(startingColumn, endCol)):
#             result.append(array[endRow][col])

#         for row in reversed(range(startingRow + 1, endRow)):
#             result.append(array[row][startingColumn])

#         startingRow += 1
#         endRow -= 1
#         startingColumn += 1
#         endCol -= 1

#     return result

array = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]


# # O(N) T | O(N) S
def spiralTraverse(array):
    result = []
    spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
    return result


def spiralFill(array, startingRow, endRow, startingCol, endCol, result):
    if startingRow > endRow or startingCol > endCol:
        return

    for col in range(startingCol, endCol + 1):
        result.append(array[startingRow][col])

    for row in range(startingRow + 1, endRow + 1):
        result.append(array[row][endCol])

    for col in reversed(range(startingCol, endCol)):
        result.append(array[endRow][col])

    for row in reversed(range(startingRow + 1, endRow)):
        result.append(array[row][startingCol])

    return spiralFill(
        array, startingRow + 1, endRow - 1, startingCol + 1, endCol - 1, result
    )


print(spiralTraverse(array))
