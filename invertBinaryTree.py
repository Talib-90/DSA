# O(n) t | O(n) s
# def invertBinaryTree(tree):
#     queue = [tree]
#     while len(queue):
#         current = queue.pop(0)
#         if current in None:
#             return 
#         swapLeftAndRight(tree)
#         queue.append(tree.left)
#         queue.append(tree.right)

# def swapLeftAndRight(tree):
#     tree.left, tree.right = tree.right, tree.left


# O(n) time | O(d) s
def invertBinaryTree(tree):
    if tree is None:
        return 
    swapLeftAndRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left