# O(N) T | O(1) S
# def isMonotonic(array):
#     if len(array) <= 2:
#         return True
#     
#     direction = array[1] - array[0]
#     for i in range(2, len(array)):
#         if direction == 0:
#             direction = array[i] - array[i - 1]
#             continue
#         if breakDirection(direction, array[i - 1], array[i]):
#             return False
        
#     return True
# def breakDirection(direction, previousInt, currentInt):
#     diffenence = currentInt - previousInt
#     if direction > 0:
#         return diffenence < 0
#     return diffenence > 0

# O(N) T | O(1) S
def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isNonDecreasing = False
            
        if array[i] > array[i - 1]:
            isNonIncreasing = False
    return isNonDecreasing or isNonIncreasing



array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
print(isMonotonic(array))