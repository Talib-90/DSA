# Worst O(N) T | O(N) S

# def closestValueInBST(tree, target):
#     return closestValueInBSTHelper(tree, target, float("inf"))

# def closestValueInBSTHelper(tree, target, closest):
#     if tree is None:
#         return closest
#     if abs(target - closest) > abs(target - tree.value):
#         closest = tree.value
#     elif target < tree.value:
#         return closestValueInBSTHelper(tree.left, target, closest)
#     elif target > tree.value:
#         return closestValueInBSTHelper(tree.right, target, closest)
#     return closest

# Worst O(N) T | O(N) S
def  closestValueBST(tree, target):
    return closestValueBSTHelper(tree, target, float("inf"))

def closestValueBSTHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest =  currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest
