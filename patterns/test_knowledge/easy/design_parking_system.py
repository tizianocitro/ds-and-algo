# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/design-parking-system-easy

'''Problem:
Design a parking system for a parking lot that has three types of parking spaces: big, medium, and small.
Each of these parking spaces has a limited number of slots available.

Implement Solution class constructor and the below methods:
- Solution(int big, int medium, int small):
    Initializes an object of the Solution class.
    This constructor receives the total number of available slots for each type of parking space: big, medium, and small.
- bool addCar(int carType):
    This method takes in an integer carType, which can be either 1 (big), 2 (medium), or 3 (small).
    It checks whether there is a free parking space available for the specified car type.
    If a slot is available, the car is parked, and the method returns true; otherwise, it returns false.

Constraints:
- 0 <= big, medium, small <= 1000
- carType is 1, 2, or 3
- At most 1000 calls will be made to addCar

Input:
    ["Solution", "addCar", "addCar", "addCar", "addCar"]
    [[2, 1, 1], [1], [2], [3], [2], [1]]
Output: [null, true, true, true, false, true]
Explanation:
    The parking system is initialized with 2 big slots, 1 medium slot, and 1 small slot.
    addCar(1): A big car parks successfully (true).
    addCar(2): A medium car parks successfully (true).
    addCar(3): A small car parks successfully (true).
    addCar(2): There is no parking slot available for medium car. So, it returns false.
    addCar(1): A big car parks successfully (true).

Input:
    ["Solution", "addCar", "addCar", "addCar", "addCar"]
    [[0, 2, 1], [3], [2], [2], [1]]
Output: [null, true, true, true, false]
Explanation:
    The parking system is initialized with 0 big slots, 2 medium slots, and 1 small slot.
    addCar(3): A small car parks successfully (true).
    addCar(2): A medium car parks successfully (true).
    addCar(2): Another medium car parks successfully in the remaining medium slot (true).
    addCar(1): A big car cannot park because there are no big slots available (false).

Input:
    ["Solution", "addCar", "addCar", "addCar", "addCar"]
    [[1, 0, 1], [2], [3], [3], [1]]
Output: [null, false, true, false, true]
Explanation:
    The parking system is initialized with 1 big slot, 0 medium slots, and 2 small slots.
    addCar(2): A medium car cannot park because there are no medium slots available (false).
    addCar(3): A small car parks successfully (true).
    addCar(3): All small car slots are occupied. So, it can't be parked.
    addCar(1): A big car parks successfully in the only available big slot (true).
'''

# solution one
# Complexity:
# O(1) time for both addCar and __init__ methods
# O(1) space because the slots list has a fixed size of 3
class Solution:
    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]

    def addCar(self, car_type: int) -> bool:
        # slots start from 1, but list index starts from 0
        slot_ix = car_type - 1
        if self.slots[slot_ix] < 1:
            return False

        self.slots[slot_ix] -= 1
        return True