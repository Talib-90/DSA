# O(N) T | O(1) S
def moveElementToEnd(array, element):
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == element:
            j -= 1
        if array[i] == element:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array

array = [2, 1, 2, 2, 2, 3, 4, 2]
element = 1
print(moveElementToEnd(array, element))