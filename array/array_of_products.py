# !difficulty: medium

# Write a function that takes in a non-empty array of integers and returns an array of the same length,
# where each element in the output array is equal to the product of every other number in the input array.
# In other words, the value at output[i] is equal to the product of every number in the input array other than input[i].
# Solve this problem without using division.

# Input:  array = [5, 1, 4, 2]
# Output: [8, 40, 10, 20]
# 8 is equal to 1 x 4 x 2
# 40 is equal to 5 x 4 x 2
# 10 is equal to 5 x 1 x 2
# 20 is equal to 5 x 1 x 4

# solution one with less memory consumption
# Same as next solution but now we use only one array because we write the content
# of leftProducts in products and then multiply the values in products with what would have been the values of rightProducts.
# Complexity
# O(n) time - where n is the length of the input array
# O(n) space - where n is the length of the newly created array
def arrayOfProducts(array):
    length = len(array)
    products = [1 for _ in range(length)]

    leftProduct = 1
    for i in range(length):
        products[i] = leftProduct
        leftProduct *= array[i]

    rightProduct = 1
    for i in reversed(range(length)):
        products[i] *= rightProduct
        rightProduct *= array[i]

    return products

# solution two
# leftProducts[i] will store the product of all the elements preceding i.
# rightProducts[i] will store the product of all the elements following i.
# Thus to compute the i-th product we just need to compute the product between leftProducts[i] and rightProducts[i].
# Complexity
# O(n) time - where n is the length of the input array
# O(n) space - where n is the length of the 3 newly created arrays
def arrayOfProducts(array):
    length = len(array)
    products = [1 for _ in range(length)]
    leftProducts = [1 for _ in range(length)]
    rightProducts = [1 for _ in range(length)]

    leftProduct = 1
    for i in range(length):
        leftProducts[i] = leftProduct
        leftProduct *= array[i]

    rightProduct = 1
    for i in reversed(range(length)):
        rightProducts[i] = rightProduct
        rightProduct *= array[i]
    
    for i in range(length):
        products[i] = leftProducts[i] * rightProducts[i]

    return products

# solution three, brute force
# Complexity
# O(n^2) time - where n is the length of the input array
# O(n) space - where n is the length of the newly created array
def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    for i in range(len(array)):
        product = 1
        l = i - 1
        r = i + 1
        while l >= 0:
            product *= array[l]
            l -= 1
        while r <= len(array) - 1:
            product *= array[r]
            r += 1
        products[i] = product
    return products
        
