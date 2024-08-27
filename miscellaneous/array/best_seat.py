# !difficulty: medium

# You walk into a theatre you're about to see a show in.
# The usher within the theatre walks you to your row and mentions you're allowed to sit anywhere within the given row.
# Naturally you'd like to sit in the seat that gives you the most space.
# You also would prefer this space to be evenly distributed on either side of you
# (e.g. if there are three empty seats in a row, you would prefer to sit in the middle of those three seats).
# Given the theatre row represented as an integer array, return the seat index of where you should sit.
# Ones represent occupied seats and zeroes represent empty seats.
# You may assume that someone is always sitting in the first and last seat of the row.
# Whenever there are two equally good seats, you should sit in the seat with the lower index. If there is no seat to sit in, return -1. The given array will always have a length of at least one and contain only ones and zeroes.

# Input:
# seats = [1, 0, 1, 0, 0, 0, 1]
# Output:
# 4 // You should sit in seat 3 because there are three empty seats closest to you.

# Complexity
# O(n) time - where n is the number of seats
# O(1) space - because we are not using any extra space

# solution one with index window
def bestSeat(seats):
    maxSpace = [0, 0]
    l, r = 0, 0

    for i in range(len(seats)):
        if seats[i] == 1:
            lMax, rMax = maxSpace
            if rMax - lMax < r - l or lMax == 0:
                maxSpace = [l, r]
            l, r = 0, 0
            continue
        if l == 0:
            l, r = i, i
            continue
        r += 1

    lMax, rMax = maxSpace
    if lMax == 0:
        return -1

    # Equivalent to return lBest + int(((rBest - lBest) / 2))
    return (lMax + rMax) // 2

# solution two with left reference
def bestSeat(seats):
    bestSeat = -1
    maxSpace = 0
    left = 0

    while left < len(seats):
        right = left + 1
        while right < len(seats) and seats[right] == 0:
            right += 1
        
        availableSpace = right - left - 1
        if availableSpace > maxSpace:
            bestSeat = (left + right) // 2
            maxSpace = availableSpace
        left = right
    
    return bestSeat
