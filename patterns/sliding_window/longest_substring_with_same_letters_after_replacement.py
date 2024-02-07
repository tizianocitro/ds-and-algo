# !difficulty: hard

'''Problem:
Given a string with lowercase letters only, if you are allowed to replace no more than k letters with any letter,
find the length of the longest substring having the same letters after replacement.

Input: string = "aabccbb", k = 2  
Output: 5  
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Input: string = "abccde", k = 1  
Output: 3  
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
'''

# solution two
# Complexity:
# O(n) time - because we are iterating through the string once
# O(1) space
class Solution:
    def findLength(self, str1, k):
        max_length = 0
        current = str1[0]
        replacements = k
        start, end = 0, 0

        # while because we need to move the end pointer back to the start
        # when we exhaust the replacements and change the current character
        while end < len(str1):
            if str1[end] != current and replacements > 0:
                replacements -= 1
            elif str1[end] != current and replacements == 0:
                replacements = k
                while str1[start] == current:
                    start += 1
                else:
                    current = str1[start]
                    end = start

            # if you reach the end of the string and you still have replacements,
            # you can start moving the start pointer to the left to exhaust the replacements
            # and increase the length of the substring
            while end == len(str1) - 1 and start > 0 and replacements > 0:
                start -= 1
                replacements -= 1
            
            max_length = max(max_length, end - start + 1)
            end += 1

        return max_length

'''
We use a HashMap to count the frequency of each letter.
1. We iterate through the string to add one letter at a time in the window.
2. We also keep track of the count of the maximum repeating letter in any window (let’s call it maxRepeatLetterCount).
3. So, at any time, we know that we do have a window with one letter repeating maxRepeatLetterCount times; this means we should try to replace the remaining letters.
    3.1. If the remaining letters are less than or equal to k, we can replace them all.
    3.2. If we have more than k remaining letters, we should shrink the window as we cannot replace more than k letters. 

While shrinking the window, we don’t need to update maxRepeatLetterCount.
Since we are only interested in the longest valid substring, our sliding windows do not have to shrink, even if a window may cover an invalid substring.
Either we expand the window by appending a character to the right or we shift the entire window to the right by one.
We only expand the window when the frequency of the newly added character exceeds the historical maximum frequency (from a previous window that included a valid substring).
In other words, we do not need to know the exact maximum count of the current window.
The only thing we need to know is whether the maximum count exceeds the historical maximum count, and that can only happen because of the newly added char.
'''
# solution two more alegant but more complex
# Complexity:
# O(n) time - because we are iterating through the string once
# O(1) space - because the frequency_map will have at most 26 characters (lowercase letters)
class Solution:
    def findLength(self, str1, k):
        window_start, max_length, max_repeat_letter_count = 0, 0, 0
        frequency_map = {}

        # Try to extend the range [window_start, window_end]
        for window_end in range(len(str1)):
            char = str1[window_end]
            # equivalent to frequency_map[char] = frequency_map.get(char, 0) + 1
            if char not in frequency_map:
                frequency_map[char] = 0
            frequency_map[char] += 1

            # we don't need to place the maxRepeatLetterCount under the below 'if' because while shrinking the window, we don’t need to update maxRepeatLetterCount.
            # Since we are only interested in the longest valid substring, our sliding windows do not have to shrink, even if a window may cover an invalid substring.
            # Either we expand the window by appending a character to the right or we shift the entire window to the right by one.
            # We only expand the window when the frequency of the newly added character exceeds the historical maximum frequency (from a previous window that included a valid substring).
            # In other words, we do not need to know the exact maximum count of the current window.
            # The only thing we need to know is whether the maximum count exceeds the historical maximum count, and that can only happen because of the newly added char.
            max_repeat_letter_count = max(
                max_repeat_letter_count, frequency_map[char])

            # Current window size is from window_start to window_end, overall we have a letter
            # which is repeating 'max_repeat_letter_count' times, this means we can have a window
            # which has one letter repeating 'max_repeat_letter_count' times and the remaining
            # letters we should replace. If the remaining letters are more than 'k', it is the
            # time to shrink the window as we are not allowed to replace more than 'k' letters
            
            # Also, in this case, you will exceed k by 1 at a time, so 'if' is sufficient, but you can also use 'while'
            # while window_end - window_start + 1 - max_repeat_letter_count > k:
            if window_end - window_start + 1 - max_repeat_letter_count > k:
                char = str1[window_start]
                frequency_map[char] -= 1
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)
        return max_length
