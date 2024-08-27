# !difficulty: easy

'''
Write a function that takes in a non-empty string and returns its run-length encoding.
From Wikipedia, "run-length encoding is a form of lossless data compression in which runs of data are stored as a single data value and count, rather than as the original run."
For this problem, a run of data is any sequence of consecutive, identical characters.
So the run "AAA" would be run-length-encoded as "ЗА" .
To make things more complicated, however, the input string can contain all sorts of special characters, including numbers.
And since encoded data must be decodable, this means that we can't naively run-length-encode long runs.
For example, the run"AAAAAAAAAAAA" (12A), can't naively be encoded as "12A", since this string can be decoded as either "AAAAAAAAAAAA" "1AA".
Thus, long runs (runs of 10 or more characters) should be encoded in a split fashion; the aforementioned run should be encoded as "9A3A".

Input: "AAAAAAAAAAAAABBCCCCDD"
Output: "9A4A2B4C2D"
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input string
# O(n) space - where n is the length of the input string for the encoded array
def runLengthEncoding(string):
    encoded = []
    currentChar = string[0]
    currentRunLength = 1

    for i in range(1, len(string)):
        char = string[i]
        if currentChar == char:
            currentRunLength += 1
            if currentRunLength <= 9:
                continue
        encoded.append(str(currentRunLength - 1 if currentRunLength > 9 else currentRunLength))
        encoded.append(currentChar)
        currentRunLength = 1
        if currentChar != char:
            currentChar = char

    # Handle last run
    encoded.append(str(currentRunLength))
    encoded.append(currentChar)

    return "".join(encoded)
        
        
