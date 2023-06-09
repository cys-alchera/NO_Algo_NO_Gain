class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        while n%3 == 0 and n >= 1:
            n = n//3
            if n==1:
                return True
        else:
            return False

"""
Runtime 85 ms
Beats 75.1%

Memory 16.2 MB
Beats 69.50%
"""