# !code: 134, !difficulty: medium, !from: https://leetcode.com/problems/gas-station/

'''Problem:
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station.
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
If there exists a solution, it is guaranteed to be unique.

Constraints:
- n == gas.length == cost.length
- 0 <= gas[i], cost[i] <= 104

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
    Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
    Travel to station 4. Your tank = 4 - 1 + 5 = 8
    Travel to station 0. Your tank = 8 - 2 + 1 = 7
    Travel to station 1. Your tank = 7 - 3 + 2 = 6
    Travel to station 2. Your tank = 6 - 4 + 3 = 5
    Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
    Therefore, return 3 as the starting index.

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
    You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
    Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
    Travel to station 0. Your tank = 4 - 3 + 2 = 3
    Travel to station 1. Your tank = 3 - 3 + 3 = 3
    You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
    Therefore, you can't travel around the circuit once no matter where you start.
'''

# solution one greedy
# Complexity:
# O(n) time - where n is the number of stations
# O(1) space
class Solution:
    def canCompleteCircuit(self, gas, cost):
        # if we do not have enough gas to cover the cost of
        # visiting all the stations, we can't complete the circuit
        if sum(gas) < sum(cost):
            return -1

        # start with an empty tank and iterate through the stations
        # by keeping track of the first index that leads to the end of
        # the circuit with a postive value for the tank
        tank = 0
        start_ix = -1
        for i in range(len(gas)):
            # get the difference between the gas and cost of visiting the station
            diff = gas[i] - cost[i]
            # add the difference to the tank
            tank += diff

            # if the tank is positive and we haven't found the start index yet
            # set the start index to the current index
            if tank >= 0 and start_ix == -1:
                start_ix = i
            # if the tank goes below 0, reset the tank and start index
            elif tank < 0:
                tank = 0
                start_ix = -1

        # just return the start index that leads to the end of the circuit
        # with a positive value for the tank
        return start_ix

# solution two brute force
# Complexity:
# O(n^2) time - where n is the number of stations
# O(1) space
class Solution:
    def canCompleteCircuit(self, gas, cost):
        # if the cost of visiting the current station is considered 0
        # we can return 0 if we have only one station but if the cost
        # can't be considered 0, we have to check if we have enough gas
        if len(gas) == 1:
            return 0 if cost[0] <= gas[0] else -1

        for i in range(len(gas)):
            if self.travel(gas, cost, i):
                return i

        return -1

    # it takes O(n) time to travel through all the stations
    # but no extra space is used
    def travel(self, gas, cost, ix):
        tank = gas[ix] - cost[ix]
        i = (ix + 1) % len(gas)

        # travel through all the stations until we reach
        # the starting station ix or we run out of gas
        # the check of tank >= 0 is to make sure we have enough gas
        # at the first station ix to move to the next station
        # so that we can ignore all the starting stations that have not enough gas
        while tank >= 0 and i != ix:
            # add the gas at the current station to the tank
            tank += gas[i]
            # if we run out of gas at the current station, we can't
            # move to the next station, so we return False
            if cost[i] > tank:
                return False
            # move to the next station and update the tank
            tank -= cost[i]
            i = (i + 1) % len(gas)

        # True if we have enough gas to travel through all the stations
        # up to the starting station ix
        return i == ix