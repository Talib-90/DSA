class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

# Time O(n) | Space O(d)
def validateBST(tree):
    return validateBSTHelper(tree, float("-inf"), float("inf"))

def validateBSTHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBSTHelper(tree.left, minValue, tree.value)
    return leftIsValid and validateBSTHelper(tree.right, tree.value, maxValue)

root = BST(10)

root.left = BST(5)
root.right = BST(15)

root.left.left = BST(2)
root.left.right = BST(5)

root.right.left = BST(13)
root.right.right = BST(22)

root.left.left.left = BST(1)

root.right.left.right = BST(14)

print(validateBST(root))