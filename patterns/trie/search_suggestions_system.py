# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/search-suggestions-system-medium

'''Problem:
Given a list of distinct strings products and a string searchWord.

Determine a set of product suggestions after each character of the search word is typed.
Every time a character is typed, return a list containing up to three product names from
the products list that have the same prefix as the typed string.

If there are more than 3 matching products, return 3 lexicographically smallest products.
These product names should be returned in lexicographical (alphabetical) order.

Constraints:
- All the strings of products are unique.
- products[i] consists of lowercase English letters.
- searchWord consists of lowercase English letters.

Input: Products: ["apple", "apricot", "application"], searchWord: "app"
Output: [["apple", "apricot", "application"], ["apple", "apricot", "application"], ["apple", "application"]]
Explanation: For the perfix 'a', "apple", "apricot", and "application" match. For the prefix 'ap', "apple", "apricot", and "application" match.
    For the prefix 'app', "apple", and "application" match

Input: Products: ["king", "kingdom", "kit"], searchWord: "ki"
Output: [["king", "kingdom", "kit"], ["king", "kingdom", "kit"]]
Explanation: All products starting with "k" are "king", "kingdom", and "kit".
    The list remains the same for the 'ki' prefix.

Input: Products: ["fantasy", "fast", "festival"], searchWord: "farm"
Output: [["fantasy", "fast", "festival"], ["fantasy", "fast"], [], []]
Explanation: Initially, "fantasy", "fast", and "festival" match 'f'. Moving to 'fa', only "fantasy" and "fast" match.
    No product matches with "far", and "farm".
'''

# solution one
# Complexity:
# O(sw) time - where s is the length of the searchWord and w is the length of the longest word in the products
# O(sw) space - to store the suggestions
class TrieNode:
    # initialize a TrieNode with a dictionary to hold children nodes and a flag to mark word's end
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    # the complexity of this fully depends on the _search() method
    # it takes O(3 * m) time to search for a prefix in the trie because
    # it just iterates through the characters of the prefix, which will always
    # be less than or equal to the length of the longest word in the trie
    # it takes O(3 * m) space to store the prefix and then the up to 3 suggestions
    def search(self, prefix):
        # if the prefix is empty, return no suggestions
        if len(prefix) < 1:
            return []

        # iterate until the last character of the prefix
        # if the prefix is not in the trie, return no suggestions
        # while exploring the trie, store the characters in a suggestion
        # that will be used as a prefix for all suggestions
        suggestion = []
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
            suggestion.append(ch)

        # search for suggestions starting from the last character of the prefix
        suggestions = []
        self._search(node, suggestion, suggestions)
        return suggestions

    # it takes O(3 * m) time to find the top 3 suggestions for a given prefix
    # where m is the length of the longest word in the trie
    # it takes O(3 * m) space to store the suggestions because we are storing
    # up to 3 suggestions, each suggestion has a length less or equal to the
    # length of the longest word in the trie
    def _search(self, node, suggestion, suggestions):
        # if we have found 3 suggestions, stop searching
        if len(suggestions) == 3:
            return

        # if we have reached the end of a word, add it to the suggestions
        if node.is_end:
            suggestions.append(''.join(suggestion))

        # recursively search the children nodes in search of suggestions
        for ch in sorted(node.children.keys()):
            # append the character to the current suggestion
            suggestion.append(ch)
            # search for suggestions containing the current character
            self._search(node.children[ch], suggestion, suggestions)
            # remove the character from the current suggestion to backtrack
            suggestion.pop()

class Solution:
    def suggestedProducts(self, products, searchWord):
        # build a trie with the products
        # O(nm) time - where n is the number of products
        # and m is the length of the longest word
        # O(nm) space - n and m are the same as above
        trie = Trie()
        for product in products:
            trie.insert(product)

        # O(sw) time - where s is the length of the searchWord and
        # w is the length of the longest word in the products
        # O(sw) space - to store the suggestions, s and w are the same as above
        result = []
        # for each character in the search word, find the top 3 suggestions
        for i in range(len(searchWord)):
            suggestions = trie.search(searchWord[:i+1])
            # print suggestions per each char
            # print(searchWord[:i+1], ' -> ', suggestions)
            result.append(suggestions)

        return result

# solution two
# Complexity:
# O(sw) time - where s is the length of the searchWord and w is the length of the longest word in the products
# O(sw) space - to store the suggestions
class TrieNode:
    # initialize a TrieNode with a dictionary to hold children nodes and a flag to mark word's end
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

    def dfs(self, node, prefix, list):
        # stop if we already have 3 suggestions
        if len(list) == 3:
            return
        # add the word to the list if we're at the end of a word
        if node.isEnd:
            list.append(prefix)

        # recursively search for all possible characters
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            if ch in node.children:
                self.dfs(node.children[ch], prefix + ch, list)

    def search(self, prefix):
        node = self.root
        # traverse the trie to the end of the prefix
        for ch in prefix:
            if ch not in node.children:
                # return an empty list if the prefix is not present
                return []
            node = node.children[ch]

        list = []
        # start DFS from the end of the current prefix
        self.dfs(node, prefix, list)
        return list

class Solution:
    def suggestedProducts(self, products, searchWord):
        trie = Trie()
        # build a trie with the products
        for product in products:
            trie.insert(product)

        result = []
        prefix = ''
        # for each character in the search word, find the top 3 suggestions
        for ch in searchWord:
            prefix += ch
            result.append(trie.search(prefix))

        return result
