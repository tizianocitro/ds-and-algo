# !difficulty: easy

'''
A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing English letters (lower or upper-case),
return true if sentence is a pangram, or false otherwise.
Note: The given sentence might contain other characters like digits or spaces, your solution should handle these too.

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true (Explanation: sentence contains at least one of every letter of the English alphabet)
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the sentence
# O(1) space - because O(c) space, where c is the length of the alphabet, so O(1) space
class Solution:
    def checkIfPangram(self, sentence):
        letters = (ord("z") - ord("a")) + 1 # This is 26 (the length of the alphabet)
        uniqueLetters = set([]) # Always a length of 26 (the alphabet)
        for c in sentence:
            lowerC = c.lower()
            if lowerC.isalpha() and lowerC not in uniqueLetters:
                uniqueLetters.add(lowerC)    
        return len(uniqueLetters) == letters
    
# solution two
# Complexity:
# O(n) time - where n is the length of the sentence
# O(1) space - because O(c) space, where c is the length of the alphabet, so O(1) space
class Solution:
    def checkIfPangram(self, sentence):
        a = ord("a")
        z = ord("z")
        letters = (z - a) + 1
        uniqueLetters = set([]) # Always a length of 26 (the alphabet)
        for c in sentence:
            lowerC = c.lower()
            ordC = ord(lowerC)
            if ordC < a or ordC > z:
                continue
            if lowerC not in uniqueLetters:
                uniqueLetters.add(lowerC)    
        return len(uniqueLetters) == letters
