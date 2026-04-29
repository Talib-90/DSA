# O(N) T | O(1) S
def singleCycleCheck(array):
    elementVisited = 0
    currentIdx = 0
    while elementVisited < len(array):
        if elementVisited > 0 and currentIdx == 0:
            return False
        elementVisited += 1
        currentIdx = getNextIdx(currentIdx, array)
    return currentIdx == 0

def getNextIdx(currIdx, array):
    jump = array[currIdx]
    nextIdx = (currIdx + jump) % len(array)
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)

array = [2, 3, 1, -4, -4, 2]
print(singleCycleCheck(array))