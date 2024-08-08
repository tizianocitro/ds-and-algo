# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6385dac84a29c96532f7c6b7

'''Problem:
Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words.
It is given that all words are of the same length.

Input: string = "catfoxcat", words = ["cat", "fox"]  
Output: [0, 3]  
Explanation: The two substring containing both the words are "catfox" & "foxcat".

Input: string = "catcatfoxfox", words = ["cat", "fox"]  
Output: [3]
Explanation: The only substring containing both the words is "catfox".
'''

# solution one
# Complexity:
# O(n * m * l) time - where n is the number of characters in the string, m is the number of words, and l is the length of a word
# O(m) space - because, at most, we will be storing all the words in the two dictionaries
# In the worst case, we also need O(n) space for the resulting result_indices list, so the overall space complexity of the algorithm will be O(n + m).
class Solution:
    def findWordConcatenation(self, str1, words):
        if len(words) == 0 or len(words[0]) == 0:
            return []

        word_frequency = {}
        for word in words:
            word_frequency[word] = word_frequency.get(word, 0) + 1

        result_indices = []
        words_count = len(words)
        word_length = len(words[0])
        concatenation_min_length = words_count * word_length

        # loops over the indices of str1 considering only those indices that can potentially form a concatenation of the words.
        # This optimization helps avoid unnecessary iterations.
        # Consider only the indexes that can produce a substring long enough
        # to be a concatenation of the words, so if we have a string long 15
        # and 2 words of 3 characters we will not range over the last 5 indexes
        # because to be a concatenation a substring must have at least 6 characters.
        # Adding 1 accounts for the possibility of starting the concatenation at the very end of str1
        for i in range((len(str1) - concatenation_min_length) + 1):
            # track the frequency of words encountered in the current substring
            words_seen_frequency = {}

            # for each starting index, traverse through the words list
            # to check if the concatenation of words starting from the current i includes all words
            # i is the starting index for the substring, while j is the number of the word I'm looking for (the first, second, etc.)
            for j in range(0, words_count):
                # this will be for examples 0, then 6 (0 - 5 is a substring of two concatenated words),
                # then 9 (0 - 8 is a substring of three concatenated words), when i = 0
                next_word_index = i + j * word_length

                # get the next word from the string
                word = str1[next_word_index:next_word_index + word_length]
                
                # break if we don't need this word
                # (e.g., if we have 'catfox' and have now i = 1, we start with word = 'atf')
                if word not in word_frequency:
                    break

                # add the word to the 'words_seen' map
                words_seen_frequency[word] = words_seen_frequency.get(word, 0) + 1

                # no need to process further if the word has higher frequency than required
                # or if it is not present at all
                if words_seen_frequency[word] > word_frequency.get(word, 0):
                    break

                # store index if we have found all the words
                # j will range up to words_count - 1, if we get here with j = words_count - 1,
                # it means all words are concatenated within the substring
                if j + 1 == words_count:
                    result_indices.append(i)

        return result_indices