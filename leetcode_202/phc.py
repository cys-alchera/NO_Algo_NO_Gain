"""
2023-05-20
Leetcode 202: Happy Number
https://leetcode.com/problems/happy-number/
Park Hee Chan
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        Starting with any positive integer, replace the number by the sum of the squares of its digits.
        Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
        Those numbers for which this process ends in 1 are happy.
        '''
        if n == 1:
            return True

        memoization = list()
        return self.happy_cycle(n, memoization)

    def happy_cycle(self, n, memoization):
        print(n, memoization)
        if n in memoization:
            return False

        sum_of_squares = 0
        for s in str(n):
            sum_of_squares += (int(s) * int(s))

        if sum_of_squares == 1:
            return True

        return self.happy_cycle(sum_of_squares, memoization + [n])


'''
Runtime 41 ms
Beats 48.8%

Memory 16.5 MB
Beats 5.96%
'''