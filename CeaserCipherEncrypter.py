# O(N) time | O(N) space
# def ceaserCipherEncryptor(string, key):
#     newLetters = []
#     newKey = key % 26
#     for letter in string:
#         newLetters.append(getNewLetter(letter, newKey))
#     return "".join(newLetters)

# def getNewLetter(string, key):
#     newletterCode = ord(string) + key
#     return chr(newletterCode) if newletterCode <= 122 else chr(96 + newletterCode % 122)

# O(N) time | O(N) space
def ceaserCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey, alphabet))
    return "".join(newLetters)

def getNewLetter(letter, key, alphabet):
    newletterCode = alphabet.index(letter) + key
    return alphabet[newletterCode] if newletterCode <= 25 else alphabet[-1 + newletterCode % 25]



st = "xyz"
key = 2
print(ceaserCipherEncryptor("xyz", 2))