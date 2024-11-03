# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/64902fec5d0034e2d16110aa

'''Problem:
Given an absolute file path in a Unix-style file system, simplify it by converting ".." to the previous directory and removing any "." or multiple slashes.
The resulting string should represent the shortest absolute path.

Input: "/a//b////c/d//././/.."
Output: "/a/b/c"

Input: "/../"
Output: "/"

Input: "/home//foo/"
Output: "/home/foo"
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input string
# O(n) space - where n is the length of the input string
class Solution:
    def simplifyPath(self, path):
        stack = []
        components = path.split('/')
        shortPath = ''

        for component in components:
            if component == '' or component == '.':
                continue
            if component == '..':
                # we do this because we need to skip the .. if the stack is empty
                # so we cannot do if component == '..' and stack: 
                # because in this wasy we would append the .. to the stack
                if stack:
                    stack.pop()
                continue
            stack.append(component)

        if not stack:
            return '/'

        for component in stack:
            shortPath += '/'
            shortPath += component

        return shortPath