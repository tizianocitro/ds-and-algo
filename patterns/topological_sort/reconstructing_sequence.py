# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/problem-challenge-1-reconstructing-a-sequence-hard

'''Problem:
Given a sequence originalSeq and an array of sequences, write a method to find if
originalSeq can be uniquely reconstructed from the array of sequences.

Unique reconstruction means that we need to find if originalSeq is the only
sequence such that all sequences in the array are subsequences of it.

Constraints:
- n == originalSeq.length
- originalSeq is a permutation of all the integers in the range [1, n].
- all the arrays of sequences are unique.
- seqs[i] is a subsequence of the the integers in the range [1, n].

Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [3, 4]]
Output: true
Explanation: The sequences [1, 2], [2, 3], and [3, 4] can uniquely reconstruct [1, 2, 3, 4], in other words,
all the given sequences uniquely define the order of numbers in the 'originalSeq'. 

Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [2, 4]]
Output: false
Explanation: The sequences [1, 2], [2, 3], and [2, 4] cannot uniquely reconstruct 
[1, 2, 3, 4]. There are two possible sequences we can construct from the given sequences:
1) [1, 2, 3, 4]
2) [1, 2, 4, 3]

Input: originalSeq: [3, 1, 4, 2, 5], seqs: [[3, 1, 5], [1, 4, 2, 5]]
Output: true
Explanation: The sequences [3, 1, 5] and [1, 4, 2, 5] can uniquely reconstruct [3, 1, 4, 2, 5].
'''

# solution one
# Complexity:
# O(nm + v + e) time, where n is the number of sequences and m is the longest of the sequences
# and v is the number of numbers and e is the number of rules that we have for them,
# since each number will give at most one rule, e is the count of numbers in all sequences
# O(v + e) space - where v is the number of numbers and e is the number of rules that we have for them
# it is the space required for the graph and in-degrees
from collections import deque

class Solution:
    def canConstruct(self, original_seq, sequences):
        # we can't construct the sequence if the original sequence is empty
        if len(original_seq) < 1:
            return True

        # it takes O(nm) time to build the graph and in-degrees
        graph, in_degrees = self.buildGraph(original_seq, sequences)
        # if we have a different number of nodes in the graph than the original sequence
        # then we can't construct the unique sequence
        if len(in_degrees) != len(original_seq):
            return False

        sources = deque()
        for num in in_degrees.keys():
            if in_degrees[num] == 0:
                sources.append(num)

        # this takes O(v + e) time, where v is the number of numbers
        # and e is the number of rules that we have for them,
        # since each number will give at most one rule,
        # e is the count of numbers in all sequences
        sorted_order = []
        while sources:
            # more than one sources mean, there is more than one
            # way to reconstruct the sequence
            if len(sources) > 1:
                return False

            current_num = sources.popleft()

            # the next source (or number) is different from the original sequence
            current_num_ix = len(sorted_order)
            if original_seq[current_num_ix] != current_num:
                return False

            sorted_order.append(current_num)
            for child in graph[current_num]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    sources.append(child)

        # if sorted_order's size is not equal to original sequence's size,
        # there is no unique way to construct
        return len(sorted_order) == len(original_seq) 

    # build the graph and in-degrees, it takes O(nm) time
    # where n is the number of sequences and m is the longest of the sequences
    def buildGraph(self, original_seq, sequences):
        in_degrees, graph = {}, {}
        for num in original_seq:
            in_degrees[num] = 0
            graph[num] = []

        # each num that follows the current num in the sequence
        # is a child of the current num
        for seq in sequences:
            for i in range(len(seq) - 1):
                parent, child = seq[i], seq[i + 1]
                graph[parent].append(child)
                in_degrees[child] += 1

        return graph, in_degrees

# solution two with backtracking
# Complexity:
# O(v! * e) time - where v is the number of tasks and e is the number of prerequisites
# the e term is needed because in each recursive call, at max, we remove (and add back) all the edges.
# O(v! * e) space - since we have to store all of the topological sorts
from collections import deque

class Solution:
    def __init__(self):
        self.orders = []

    def canConstruct(self, original_seq, sequences):
        # we can't construct the sequence if the original sequence is empty
        if len(original_seq) < 1:
            return False

        # it takes O(nm) time to build the graph and in-degrees
        graph, in_degrees = self.buildGraph(original_seq, sequences)
        # if we have a different number of nodes in the graph than the original sequence
        # then we can't construct the unique sequence
        if len(in_degrees) != len(original_seq):
            return False

        # find all sources, i.e., all vertices with 0 in-degrees
        sources = deque()
        for num in in_degrees.keys():
            if in_degrees[num] == 0:
                sources.append(num)

        # find all sequences that can be constructed from the graph
        sorted_order = []
        self.backtrack(sources, graph, in_degrees, original_seq, sorted_order)

        # if we have more than one sequence, then we have multiple sequences
        # that can be constructed, so the orginal sequence is not unique
        if len(self.orders) < 0 or len(self.orders) > 1:
            return False

        # check if the only sequence that can be constructed is the original sequence
        return self.orders[0] == original_seq

    # backtracking to find all sequences
    def backtrack(self, sources, graph, in_degrees, original_seq, sorted_order):
        # if we have a complete sequence, add it to the list of sequences
        if len(sorted_order) == len(original_seq):
            self.orders.append(sorted_order.copy())

        # iterate through all sources
        if sources:
            for source in sources:
                sorted_order.append(source)

                # build the next sources for the recursive call
                next_sources = deque(sources)
                next_sources.remove(source)
                for child in graph[source]:
                    in_degrees[child] -= 1
                    if in_degrees[child] == 0:
                        next_sources.append(child)

                self.backtrack(next_sources, graph, in_degrees, original_seq, sorted_order)

                # backtrack by removing the current source from the sorted order
                # and adding back the in-degrees for the children of the current source
                sorted_order.remove(source)
                for child in graph[source]:
                    in_degrees[child] += 1

    # build the graph and in-degrees, it takes O(nm) time
    # where n is the number of sequences and m is the longest of the sequences
    def buildGraph(self, original_seq, sequences):
        in_degrees, graph = {}, {}
        for num in original_seq:
            in_degrees[num] = 0
            graph[num] = []

        # each num that follows the current num in the sequence
        # is a child of the current num
        for seq in sequences:
            for i in range(len(seq) - 1):
                parent, child = seq[i], seq[i + 1]
                graph[parent].append(child)
                in_degrees[child] += 1

        return graph, in_degrees

