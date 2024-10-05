# !code: 380, !difficulty: medium, !from: https://leetcode.com/problems/insert-delete-getrandom-o1/

'''Problem:
Implement the RandomizedSet class:
- RandomizedSet() Initializes the RandomizedSet object.
- bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
- bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
- int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called).
  Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.

Constraints:
- -231 <= val <= 231 - 1
- At most 2 * 105 calls will be made to insert, remove, and getRandom
- There will be at least one element in the data structure when getRandom is called

Input:
    ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
    [[], [1], [2], [2], [], [1], [2], []]
Output: [null, true, false, true, 2, true, false, 2]

Explanation:
    RandomizedSet randomizedSet = new RandomizedSet();
    randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
    randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
    randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
    randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
    randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
    randomizedSet.insert(2); // 2 was already in the set, so return false.
    randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
'''

'''Note:
The structure looks quite theoretical, but it's widely used in popular statistical algorithms like Markov chain Monte Carlo and Metropolis-Hastings algorithm.
These algorithms are for sampling from a probability distribution when it's difficult to compute the distribution itself.
'''

# solution one using hash map and list
# Complexity:
# O(1) time:
# - insert: O(1) average, O(n) worst case when we need to resize the list
# - remove: O(1) average, O(n) worst case when we need to resize the list
# - getRandom: O(1)
# O(n) space - because we store all the values in the list and the map
import random

class RandomizedSet:
    def __init__(self):
        # the map stores the value and its index in the list
        # it's used for O(1) contains and index lookup
        self.map = {}
        # the list stores the values
        # it's used for O(1) random access
        self.keys = []

    def insert(self, val: int) -> bool:
        # if the value is already in the map, return False
        if val in self.map:
            return False

        # append the value to the list
        self.keys.append(val)
        # store the value and its index in the map
        self.map[val] = len(self.keys) - 1

        return True

    def remove(self, val: int) -> bool:
        # if the value is not in the map, return False
        if val not in self.map:
            return False

        # get the index of the value in the list from the map
        val_ix = self.map[val]

        # if the value is not the last one in the list
        # we get the last value from the list
        # and its index from the map
        last_val = self.keys[-1]
        last_val_ix = self.map[last_val]

        # swap the value and the last value in the list for O(1) removal using pop()
        self.keys[last_val_ix], self.keys[val_ix] = self.keys[val_ix], self.keys[last_val_ix]
        # update the index of the elements that was the last value in the map before the swap
        # to the index of the value that we are now removing, so that we won't leave a gap
        # in the list that could cause problems in the random access using list's length
        self.map[last_val] = val_ix

        # remove the value from the map and the list
        del self.map[val]
        self.keys.pop()

        return True

    def getRandom(self) -> int:
        # get a random index in the list
        ix = random.randint(0, len(self.keys) - 1)
        # return the value at that index
        return self.keys[ix]