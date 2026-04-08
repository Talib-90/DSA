listArray = [-1,22,3,7,10,5,-11,9]
target = 15

# O(N^2) T | O(1) S
def twoNumberSum(array, target):
    for i in range(len(array)):
        for j in range(i + 1, len(array) - 1):
            if array[i] + array[j] == target:
                return [array[i], array[j]]
    return []

print(twoNumberSum(listArray, target))

# O(N)T | O(N)S
# def twoNumberSum(array, target):
#     nums = {}
#     for num in array:
#         match = target - num
#         if match in nums:
#             return [match, num]
#         else:
#             nums[num] = True
#     return []

# print(twoNumberSum(listArray, target))

# O(NlogN)T | O(1)S 
# def twoNumberSum(array, target):
#     array.sort()
#     L = 0
#     R = len(array) - 1
#     while L < R:
#         match = array[L] + array[R]
#         if match == target:
#             return [array[L], array[R]]
#         elif match < target:
#             L += 1
#         else:
#             R -= 1
#     return []
# print(twoNumberSum(listArray, target))