# O(n) t | O(n) s
# def maxSubsetNoAdjecentSum(array):
#     if not len(array):
#         return 
#     elif len(array) == 1:
#         return array[0]
#     maxSums = array[:]
#     maxSums[1] = max(maxSums[0], maxSums[1])
#     for i in range(2, len(array)):
#         maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + maxSums[i])
#     return maxSums[-1]

# O(n) t | O(1) S
def maxSubsetNoAdjecentSum(array):
    if not len(array):
        return 
    elif len(array) == 1:
        return array[0]
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first


array = [7, 10, 12, 7, 9, 14]
print(maxSubsetNoAdjecentSum(array))