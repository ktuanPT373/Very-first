'''
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.

Input: n = 10, k = 1, maxPts = 10
Output: 1.00000

This solution is time limit exceeded on leetcode, but it works well for medium and small test case. 
I cannot come up with the better solution for this problem

'''
import sys

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        hashmap = {}
        def dfs(score):
            if score >= k:
                return 1 if score <= n else 0
            if score in hashmap:
                return hashmap[score]
            prob = 0
            for i in range(1,maxPts+1):
                prob += dfs(score+i) 
            hashmap[score] = prob/maxPts
            return hashmap[score]
        return dfs(0)
print(sys.argv)