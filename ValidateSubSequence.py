array = [2, -1, 5, 6, 10, 13, 19, 22, 18, 15]
sequence = [-1, 6, 19, 15]

# O(N) time | O(N) space
# def ValidateSubSequence(array, sequence):
#     arrayIdx = 0
#     seqIdx = 0
#     while arrayIdx < len(array) and seqIdx < len(sequence):
#         if array[arrayIdx] == sequence[seqIdx]:
#             seqIdx += 1
#         arrayIdx += 1
#     return seqIdx == len(sequence)

def ValidateSubSequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)