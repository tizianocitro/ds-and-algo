# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/alien-dictionary-hard

'''Problem:
There is a dictionary containing words from an alien language for which we don’t know the ordering of the letters.

Given a list of strings words from the alien language's dictionary.
All strings in words are sorted lexicographically by the rules of this new language.
Each word consists of only lowercase English letters.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules.

It is given that the input is a valid dictionary and there exists an ordering among its letters.

Input: Words: ["ba", "bc", "ac", "cab"]
Output: bac
Explanation: Given that the words are sorted lexicographically by the rules of the alien language, so
from the given words we can conclude the following ordering among its characters:
1. From "ba" and "bc", we can conclude that 'a' comes before 'c'.
2. From "bc" and "ac", we can conclude that 'b' comes before 'a'
From the above two points, we can conclude that the correct character order is: "bac"

Input: Words: ["cab", "aaa", "aab"]
Output: cab
Explanation: From the given words we can conclude the following ordering among its characters:
1. From "cab" and "aaa", we can conclude that 'c' comes before 'a'.
2. From "aaa" and "aab", we can conclude that 'a' comes before 'b'
From the above two points, we can conclude that the correct character order is: "cab"

Input: Words: ["ywx", "wz", "xww", "xz", "zyy", "zwz"]
Output: ywxz
Explanation: From the given words we can conclude the following ordering among its characters:
1. From "ywx" and "wz", we can conclude that 'y' comes before 'w'.
2. From "wz" and "xww", we can conclude that 'w' comes before 'x'.
3. From "xww" and "xz", we can conclude that 'w' comes before 'z'
4. From "xz" and "zyy", we can conclude that 'x' comes before 'z'
5. From "zyy" and "zwz", we can conclude that 'y' comes before 'w'
From the above five points, we can conclude that the correct character order is: "ywxz"
'''

# solution one using a list to store the children
# Complexity:
# O(nm + (v + n)) time where n is the number of words, m is the average length of the words
# and v is the number of letters in the words. Considering that we have only 26 letters, v = 26
# So the time complexity is O(nm) + O(26 + n) = O(nm)
# O(v + n) space where v is the number of letters and n is the number of words,
# since we have only 26 letters, the space complexity is O(n)
from collections import deque

class Solution:
    def findOrder(self, words):
        if len(words) < 1:
            return ''

        # create a set of all the letters in the words,
        # given that we have only 26 letters, it takes O(1) time
        letters = set(''.join(words))

        # it takes O(n * m) time where n is the number of words
        # and m is the average length of the words
        graph, in_degrees = self.buildGraph(words, letters)

        sources = deque()
        for node in in_degrees.keys():
            if in_degrees[node] == 0:
                sources.append(node)

        # we have to iterate over all the letters in the graph,
        # it takes O(v) where v is the number of letters
        # then, for each letter we have to iterate over it's children
        # that represent the rules, and in total each word can give at most 1 rule
        # so we will have at most n rules where n is the number of words
        # so this part takes O(v + n) time
        sorted_order = []
        while sources:
            node = sources.popleft()
            sorted_order.append(node)

            for child in graph[node]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    sources.append(child)

        if len(sorted_order) != len(letters):
            return ''

        return ''.join(sorted_order)

    # we have to iteratere through all the words, and for each word, we have
    # to iterate through the characters of the word until we find the first different
    # character between the two words, it takes O(n * m) time where n is the number of words
    def buildGraph(self, words, letters):
        in_degrees = {node: 0 for node in letters}
        graph = {node: [] for node in letters}

        # find ordering of characters from adjacent words
        for ix in range(len(words) - 1):
            w1, w2 = words[ix], words[ix + 1]
            # iterate through the two words using the shorter one as the limit
            min_word_len = min(len(w1), len(w2))
            for i in range(min_word_len):
                # ch1 is the parent, ch2 is the child
                ch1, ch2 = w1[i], w2[i]
                # if the two characters are different
                if ch1 != ch2:
                    # put the child into it's parent's list
                    graph[ch1].append(ch2)
                    in_degrees[ch2] += 1
                    # only the first different character between the two words will help us
                    break

        return graph, in_degrees

# solution two using a set to store the children
# Complexity:
# O(nm + (v + n)) time where n is the number of words, m is the average length of the words
# and v is the number of letters in the words. Considering that we have only 26 letters, v = 26
# So the time complexity is O(nm) + O(26 + n) = O(nm)
# O(v + n) space where v is the number of letters and n is the number of words,
# since we have only 26 letters, the space complexity is O(n)
from collections import deque

class Solution:
    def findOrder(self, words):
        if len(words) < 1:
            return ''

        # create a set of all the letters in the words,
        # given that we have only 26 letters, it takes O(1) time
        letters = set(''.join(words))

        graph, in_degrees = self.buildGraph(words, letters)

        sources = deque()
        for node in in_degrees.keys():
            if in_degrees[node] == 0:
                sources.append(node)

        sorted_order = []
        while sources:
            node = sources.popleft()
            sorted_order.append(node)

            for child in graph[node]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    sources.append(child)

        if len(sorted_order) != len(letters):
            return ''

        return ''.join(sorted_order)

    def buildGraph(self, words, letters):
        in_degrees = {node: 0 for node in letters}
        graph = {node: set() for node in letters}

        # find ordering of characters from adjacent words
        for ix in range(len(words) - 1):
            w1, w2 = words[ix], words[ix + 1]
            # iterate through the two words using the shorter one as the limit
            min_word_len = min(len(w1), len(w2))
            for i in range(min_word_len):
                # ch1 is the parent, ch2 is the child
                ch1, ch2 = w1[i], w2[i]
                # if the child is already in the parent's list, we don't need to do anything
                # because we are using a set in this solutio
                if ch2 in graph[ch1]:
                    break
                # if the two characters are different
                if ch1 != ch2:
                    # put the child into it's parent's list
                    graph[ch1].add(ch2)
                    in_degrees[ch2] += 1
                    # only the first different character between the two words will help us
                    break

        return graph, in_degrees

# solution three using a list like solution one but without the letters set
# Complexity:
# O(nm + (v + n)) time where n is the number of words, m is the average length of the words
# and v is the number of letters in the words. Considering that we have only 26 letters, v = 26
# So the time complexity is O(nm) + O(26 + n) = O(nm)
# O(v + n) space where v is the number of letters and n is the number of words,
# since we have only 26 letters, the space complexity is O(n)
from collections import deque

class Solution:
    def findOrder(self, words):
        if len(words) == 0:
            return ''

        in_degrees = {}
        graph = {}
        for word in words:
            for ch in word:
                in_degrees[ch] = 0
                graph[ch] = []

        # populate in-degree and graph
        for i in range(0, len(words) - 1):
            # find ordering of characters from adjacent words
            w1, w2 = words[i], words[i + 1]
            for j in range(0, min(len(w1), len(w2))):
                parent, child = w1[j], w2[j]
                # if the two characters are different
                if parent != child:
                    # put the child into it's parent's list
                    graph[parent].append(child)
                    in_degrees[child] += 1
                    # only the first different character between the two words will help us 
                    break

        # find all sources i.e., all vertices with 0 in-degrees
        sources = deque()
        for node in in_degrees:
            if in_degrees[node] == 0:
                sources.append(node)

        # for each source, add it to the sorted_order and subtract one from all of its 
        # children's in-degrees if a child's in-degree becomes zero, add it to sources queue
        sorted_order = []
        while sources:
            node = sources.popleft()
            sorted_order.append(node)
            # get the node's children to decrement their in-degrees
            for child in graph[node]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    sources.append(child)

        # if sortedOrder doesn't contain all characters, there is a cyclic dependency between 
        # characters, therefore, we'll not be able to find the correct ordering of characters
        if len(sorted_order) != len(in_degrees):
            return ''

        return ''.join(sorted_order)