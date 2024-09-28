# !code: 127, !difficulty: hard, !from: https://leetcode.com/problems/word-ladder/

'''Problem:
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
- sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Constraints:
- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length
- beginWord, endWord, and wordList[i] consist of lowercase English letters
- beginWord != endWord
- All the words in wordList are unique

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
'''

# solution one using bfs
# Complexity:
# O(n * m^2) time, where n is the number of words and m is the length of each word
# O(n * m^2) time, where n is the number of words and m is the length of each word
'''Complexity Analysis
Time Complexity: O(M^2xN), where M is the length of each word and N is the total number of words in the input word list.
- For each word in the word list, we iterate over its length to find all the intermediate words corresponding to it.
  Since the length of each word is M and we have N words, the total number of iterations the algorithm takes to create all_combo_dict is MxN.
  Additionally, forming each of the intermediate word takes O(M) time because of the substring operation used to create the new string.
  This adds up to a complexity of O(M^2xN).
- Breadth first search in the worst case might go to each of the N words. For each word, we need to examine M possible intermediate words/combinations.
  Notice, we have used the substring operation to find each of the combination. Thus, M combinations take O(M^2) time.
  As a result, the time complexity of BFS traversal would also be O(M^2xN).
Combining the above steps, the overall time complexity of this approach is O(M^2xN).

Space Complexity: O(M^2xN).
- Each word in the word list would have M intermediate combinations. To create the all_combo_dict dictionary we save an intermediate word as the key
  and its corresponding original words as the value. Note, for each of M intermediate words we save the original word of length M. This simply means,
  for every word we would need a space of M^2 to save all the transformations corresponding to it. Thus, all_combo_dict would need a total space of O(M^2xN).
- Visited dictionary would need a space of O(MxN) as each word is of length M.
- Queue for BFS in worst case would need a space for all O(N) words and this would also result in a space complexity of O(MxN).
Combining the above steps, the overall space complexity is O(M^2xN) + O(MxN) + O(MxN) = O(M^2xN) space.

Optimization:
We can definitely reduce the space complexity of this algorithm by storing the indices corresponding to each word instead of storing the word itself.
'''
from collections import defaultdict, deque

class Solution(object):
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # since all words are of same length
        L = len(beginWord)

        # dictionary to hold combination of words that can be formed,
        # from any given word, by changing one letter at a time
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # key is the generic word
                # value is a list of words which have the same intermediate generic word
                all_combo_dict[word[:i] + '*' + word[i + 1:]].append(word)

        # queue for bfs
        queue = deque([(beginWord, 1)])

        # visited to make sure we don't repeat processing same word
        visited = set()
        visited.add(beginWord)

        while queue:
            current_word, level = queue.popleft()

            # for each possible position in the word
            for i in range(L):
                # intermediate words for current word
                intermediate_word = current_word[:i] + '*' + current_word[i + 1:]

                # next states are all the words which share the same intermediate state
                for word in all_combo_dict[intermediate_word]:
                    # if at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer
                    if word == endWord:
                        return level + 1

                    # otherwise, add it to the bfs queue and mark it visited
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))

                # ensures that we don’t need to revisit the same set of
                # transformations again in subsequent iterations for
                # words that share the same intermediate_word
                # thanks to this optimization, our algorithm only visits each transformation once
                # because all the words are visited through the 'for i in range(L)' loop
                # or the 'for word in all_combo_dict[intermediate_word]' loop
                all_combo_dict[intermediate_word] = []

        return 0
