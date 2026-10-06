# !code: 997, !difficulty: easy, !from: https://leetcode.com/problems/find-the-town-judge, https://neetcode.io/problems/find-the-town-judge

'''Problem:
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Constraints:
- 1 <= n <= 1000
- 0 <= trust.length <= 10^4
- trust[i].length == 2
- All the pairs of trust are unique
- ai != bi
- 1 <= ai, bi <= n

Input: n = 2, trust = [[1,2]]
Output: 2

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
'''

# solution one using degrees
# Complexity:
# O(n + m) time - where n is the number of nodes and m is the number of edges in trust
# O(n) space - for storing in_degrees and out_degrees
class Solution:
    def findJudge(self, n: int, trust) -> int:
        max_node_label = n + 1

        # we need in degrees to know how many people trust a node, as the
        # judge has in degree of n - 1 because everyone except the judge (-1) trusts the judge
        in_degrees = {node: 0 for node in range(1, max_node_label)}
        # we need out degrees to know how many people a node trusts, as the
        # judge has out degree of 0 because the judge trusts no one
        out_degrees = {node: 0 for node in range(1, max_node_label)}

        for src, dest in trust:
            in_degrees[dest] += 1
            out_degrees[src] += 1

        for node in range(1, max_node_label):
            if out_degrees[node] == 0 and in_degrees[node] == n - 1:
                return node

        return -1
