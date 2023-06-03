"""
230603
leetcode 374. guess number higher or lower.
searching problem.
Park Hee Chan
https://leetcode.com/problems/guess-number-higher-or-lower/
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
from random import randint

class Solution:
    def guessNumber(self, n: int) -> int:
        self.top = pow(2, 31) - 1
        self.bot = 1
        self.mid = int(self.top / 2)

        while True:
            if guess(self.mid) == 1:
                self.bot = self.mid
                self.mid = randint(self.bot, self.top)
                continue
            if guess(self.mid) == -1:
                self.top = self.mid
                self.mid = randint(self.bot, self.top)
                continue
            if guess(self.mid) == 0:
                return self.mid

'''
Runtime 49 ms
Beats 22.59%

Memory 16.4 MB
Beats 13.31%
'''