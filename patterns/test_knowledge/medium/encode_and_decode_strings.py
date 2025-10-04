# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/encode-and-decode-strings

'''Problem:
Given a list of strings, your task is to develop two functions: one that encodes the list of strings into a single string,
and another that decodes the resulting single string back into the original list of strings.
It is crucial that the decoded list is identical to the original one.
It is given that you can use any encoding technique to encode list of string into the single string.

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] contains any possible characters out of 256 valid ASCII characters

Input: ["apple", "banana"]
Output: ["apple", "banana"]
Explanation: When we encode the input strings ["apple", "banana"], we get a single encoded string. Decoding this encoded string should give us the original list ["apple", "banana"].

Input: ["sun", "moon", "stars"]
Output: ["sun", "moon", "stars"]
Explanation: After encoding the input list, decoding it should bring back the original list.

Input: ["Hello123", "&*^%"]
Output: ["Hello123", "&*^%"]
Explanation: Regardless of the content of the string (special characters, numbers, etc.), decoding the encoded list should reproduce the original list.
'''

# solution one using length of string
# Complexity:
# O(n) time - where n is the number of characters in the list of strings
# O(n) space - where n is the number of characters in the list of strings
class Solution:

    # O(n) time - where n is the number of characters in the list of strings
    # O(n) space - where n is the number of characters in the list of strings
    def encode(self, strs):
        encoded = ""

        # for each string in the list, encode it as 'length:string'
        for s in strs:
            count = len(s)
            encoded += str(count) + ':' + s

        return encoded

    # O(n) time - where n is the number of characters in the encoded string
    # O(n) space - where n is the number of characters in the encoded string
    def decode(self, s):
        res = []

        # len_ptr is the pointer to the current character in the string
        # at each iteration, it will point to the length of the next string
        len_ptr = 0
        while len_ptr < len(s):
            # count is the length of the next string and will extract it from
            # the encoded string by moving len_ptr until it reaches ':'
            next_str_len = 0
            while s[len_ptr] != ':':
                next_str_len = (next_str_len * 10) + int(s[len_ptr])
                len_ptr += 1

            # extract the next string from the encoded string
            start = len_ptr + 1
            end = start + next_str_len
            res.append(s[start:end])

            # move the len_ptr to the char next to the end of the
            # current string, which will be the length of the next string
            len_ptr = end

        return res
