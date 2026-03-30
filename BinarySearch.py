# O(Log(N)) T | O(Log(N)) S
# def binarySearch(array, target):
#     return binarySearchHelper(array, target, 0, len(array) -1)

# def binarySearchHelper(array, target, left, right):
#     if left > right:
#         return -1
#     middle = (left + right) // 2
#     if array[middle] == target:
#         return middle
#     elif array[middle] < target:
#         return binarySearchHelper(array, target, left, right - 1)
#     else:
#         return binarySearchHelper(array, target, middle + 1, right)

# O(Log(N)) T | O(1) S
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) -1)

def binarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            right = middle - 1
        else:
            left = middle + 1
    
    return -1