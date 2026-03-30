class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(N) T | O(N) S
def branchSum(root):
    sums = []
    calculateBranchSum(root, 0, sums)
    return sums

def calculateBranchSum(Node, runningSum, sums):
    if Node is None:
        return

    newRunningSum = runningSum + Node.value
    if Node.left is None and Node.right is None:
        sums.append(newRunningSum)
        return
    
    calculateBranchSum(Node.left, newRunningSum, sums)
    calculateBranchSum(Node.right, newRunningSum, sums)
    