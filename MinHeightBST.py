# O(NLog(N)) Time | O(n) S
# def MinHeightBst(array):
#     return constructionMinHeightBst(array, None, 0, len(array) - 1)


# def constructionMinHeightBst(array, bst, startIdx, endIdx):
#     if endIdx < startIdx:
#         return
#     midIdx = (startIdx + endIdx) // 2
#     valueToAdd = array[midIdx]
#     if bst is None:
#         bst = BST(valueToAdd)
#     else:
#         bst.insert(valueToAdd)

#     constructionMinHeightBst(array, bst, startIdx, midIdx - 1)
#     constructionMinHeightBst(array, bst, midIdx + 1, endIdx)
#     return bst

# O(n) Time | O(n) S
# def MinHeightBst(array):
#     return constructionMinHeightBst(array, None, 0, len(array) - 1)


# def constructionMinHeightBst(array, bst, startIdx, endIdx):
#     if endIdx < startIdx:
#         return
#     midIdx = (startIdx + endIdx) // 2
#     newBstNode = BST(array[midIdx])
#     if bst is None:
#         bst = newBstNode
#     else:
#         if array[midIdx] < bst.value:
#             bst.left = newBstNode
#             bst = bst.left
#         else:
#             bst.right = newBstNode
#             bst = bst.right
#     constructionMinHeightBst(array, bst, startIdx, midIdx - 1)
#     constructionMinHeightBst(array, bst, midIdx + 1, endIdx)
#     return bst

# O(n) t | O(n) s
def MinHeightBst(array):
    return constructionMinHeightBst(array, 0, len(array) - 1)


def constructionMinHeightBst(array, startIdx, endIdx):
    if endIdx < startIdx:
        return
    midIdx = (startIdx + endIdx) // 2
    bst = BST(array[midIdx])
    bst.left = constructionMinHeightBst(array, startIdx, midIdx - 1)
    bst.right = constructionMinHeightBst(array, midIdx + 1, endIdx)
    return bst




class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


array = [1, 2, 3, 5, 7, 10, 13, 14, 15, 17]
print(MinHeightBst(array))