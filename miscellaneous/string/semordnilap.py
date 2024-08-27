# !difficulty: easy

'''
Write a function that takes in a list of unique strings and returns a list of semordnilap pairs.
A semordnilap pair is defined as a set of different strings where the reverse of one word is the same as the forward version of the other.
For example the words "diaper" and "repaid" are a semordnilap pair, as are the words "palindromes" and "semordnilap".
The order of the returned pairs and the order of the strings within each pair does not matter.

Input:
words = ["diaper", "abc", "test", "cba", "repaid"]
Output:
[
    ["abc", "cba"],
    ["diaper", "repaid"],
]
'''

# solution one
# Complexity:
# O(nk) time - where n is the number of words and k is the length of the longest word
# O(n) space - where n is the number of words,
# more precisely it should be O(c) space where c is the number of unique words
def semordnilap(words):
    matchedWords = []
    reversedWords = set([])
    for w in words:
        reversedWord = w[::-1]
        if w in reversedWords and reversedWord != w:
            matchedWords.append([reversedWord, w])
            continue
        reversedWords.add(reversedWord)
    return matchedWords
