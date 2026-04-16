def remove(self, value, parentNode = None):
    currentNode = self
    while currentNode is not None:
        if value < currentNode.value:
            parentNode = currentNode
            currentNode = currentNode.left
        elif value > currentNode.value:
            parentNode = currentNode
            currentNode = currentNode.right
        else:
            if currentNode.left is not None and currentNode.right is not None:
                currentNode.value = currentNode.right.getMinValue()
                currentNode.right.remove(currentNode.value, currentNode)
            elif parentNode in None:
                if currentNode.left is not None:
                    currentNode.value = currentNode.left.value
                    currentNode.right = currentNode.left.right
                    currentNode.left = currentNode.left.left
                elif currentNode.right is not None:
                    currentNode.value = currentNode.right.value
                    currentNode.left = currentNode.right.left
                    currentNode.right = currentNode.right.right
                else:
                    currentNode.value = None
            elif parentNode.left == currentNode:
                parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
            elif parentNode.right == None:
                parentNode.right = currentNode.right if currentNode.left is not None else currentNode.right
            break
        return self

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value