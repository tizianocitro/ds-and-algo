# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/65728b1b6e4dd4f176c94c59

'''Problem:
Given a string s, remove all duplicate letters from the input string while maintaining the original order of the letters.

Additionally, the returned string should be the smallest in lexicographical order among all possible results.

Consider that s consists of lowercase English letters.

Input: "bbaac"
Output: "bac"
Explanation: Removing the extra 'b' and one 'a' from the original string gives 'bac', which is the smallest lexicographical string without duplicate letters.

Input: "zabccdef"
Output: "zabcdef"
Explanation: Removing one of the 'c's forms 'zabcdef', the smallest string in lexicographical order without duplicates.

Input: "mnopmn"
Output: "mnop"
Explanation: Removing the second 'm' and 'n' gives 'mnop', which is the smallest possible string without duplicate characters.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input string s
# O(1) space - because we know the input string will only contain lowercase English letters,
# so the frequency map, present set and result stack will all have a maximum of 26 characters
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # build the frequency map we will use to figure out whether
        # we can remove a character because it's not the last occurrence
        # so if it is a character that is lexicographically bigger than 
        # the current character, we can remove it and add it again later
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        # alternative way of building the frequency map
        # freq = {char: s.count(char) for char in set(s)}

        present, result = set(), []
        for char in s:
            # only add character if it's not already in the result
            if char not in present:
                # ensure the smallest lexicographical order
                while result and char < result[-1] and freq[result[-1]] > 0:
                    el = result.pop()
                    # we remove the element from the present set as well
                    # so that we can add it again later when we process it again
                    present.remove(el)

                result.append(char)
                # add the character to the present set to mark it as processed
                present.add(char)

            # decrement the frequency of the character, irrespective of
            # whether we add it to the result or not
            freq[char] -= 1

        return ''.join(result)