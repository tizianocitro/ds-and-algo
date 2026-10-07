# !860, !difficulty: easy, !from: https://leetcode.com/problems/lemonade-change, https://neetcode.io/problems/lemonade-change

'''Problem:
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills).
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays,
return true if you can provide every customer with the correct change, or false otherwise.

Constraints:
- 1 <= bills.length <= 10^5
- bills[i] is either 5, 10, or 20

Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

Input: bills = [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.
'''

# solution one using two counters: fives and tens
# this is a greedy approach as we always prefer to give one 10 and one 5 as change for a 20
# because we want to preserve as many 5s as possible as they are needed to give change for both 10s and 20s
# Complexity:
# O(n) time - where n is the number of bills
# O(1) space
class Solution:
    def lemonadeChange(self, bills) -> bool:
        # we don't need to track twenties, as we can never give them as change
        fives = 0
        tens = 0

        for bill in bills:
            if bill == 20:
                # prefer to give one 10 and one 5 as change
                if fives >= 1 and tens >= 1:
                    fives -= 1
                    tens -= 1
                elif fives >= 3: # we don't have 10s, so give three 5s
                    fives -= 3
                else:
                    return False

            if bill == 10:
                tens += 1

                # the only way to give change for 10 is to give one 5
                if fives < 1:
                    return False
                fives -= 1

            if bill == 5:
                fives += 1

        return True

# solution two using three counters: fives, tens, twenties
# this is a greedy approach as we always prefer to give one 10 and one 5 as change for a 20
# because we want to preserve as many 5s as possible as they are needed to give change for both 10s and 20s
# Complexity:
# O(n) time - where n is the number of bills
# O(1) space
class Solution:
    def lemonadeChange(self, bills) -> bool:
        fives = 0
        tens = 0
        twenties = 0

        for bill in bills:
            if bill == 20:
                twenties += 1

                # prefer to give one 10 and one 5 as change
                if fives >= 1 and tens >= 1:
                    fives -= 1
                    tens -= 1
                elif fives >= 3: # we don't have 10s, so give three 5s
                    fives -= 3
                else:
                    return False

            if bill == 10:
                tens += 1

                # the only way to give change for 10 is to give one 5
                if fives < 1:
                    return False
                fives -= 1

            if bill == 5:
                fives += 1

        return True