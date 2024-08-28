# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/64fd60b82322f34a81703611

'''Problem:
Given a string, determine the maximum number of times the word "balloon" can be formed using the characters from the string.
Each character in the string can be used only once.

Input: "balloonballoon"
Output: 2
Explaination: The word "balloon" can be formed twice from the given string.

Input: "bbaall"
Output: 0
Explaination: The word "balloon" cannot be formed from the given string as we are missing the character 'o' twice.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input string
# O(1) space - because, in the worst case, every character in the string is unique.
# For a string with only lowercase English letters, the maximum number of unique characters is 26.
# However, if we consider all possible ASCII characters, the number is 128.
# If we consider extended ASCII, it's 256. In any case, this is a constant number.
# Therefore, the space complexity for the hashmap is O(1) because it doesn't grow proportionally with the size of the input string.
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        min_count, target = float('inf'), "balloon"
        balloon_freq, text_freq = {}, {}

        for c in target:
            balloon_freq[c] = balloon_freq.get(c, 0) + 1
        for c in text:
            text_freq[c] = text_freq.get(c, 0) + 1

        for k, v in balloon_freq.items():
            c = text_freq.get(k, -1)
            if c < 0 or c < v:
                return 0
            min_count = min(int(c / v), min_count)

        return min_count