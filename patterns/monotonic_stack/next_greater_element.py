# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/64beb292777d61d4371e18ae

'''Problem:
Given two integer arrays nums1 and nums2, return an array answer such that answer[i] is the next greater number for every nums1[i] in nums2.
The next greater element for an element x is the first element to the right of x that is greater than x.
If there is no greater number, output -1 for that number.

The numbers in nums1 are all present in nums2 and nums2 is a permutation of nums1.

Input: nums1 = [4,2,6], nums2 = [6,2,4,5,3,7]
Output: [5,4,7]
Explanation: The next greater number for 4 is 5, for 2 is 4, and for 6 is 7 in nums2.

Input: nums1 = [9,7,1], nums2 = [1,7,9,5,4,3]
Output: [-1,9,7]
Explanation: The next greater number for 9 does not exist, for 7 is 9, and for 1 is 7 in nums2.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of nums2
# O(n) space - because of the hashmap and stack
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack, hashmap = [], {}
        
        for num in nums2:
            # pop elements from the stack that are smaller than current number
            while stack and num > stack[-1]:
                # remember the next greater element for num
                hashmap[stack.pop()] = num
            # push current number onto stack
            stack.append(num)
            
        # map the numbers in nums1 to their next greater number
        return [hashmap.get(num, -1) for num in nums1]