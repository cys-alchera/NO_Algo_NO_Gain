"""
507. Perfect Number
Lee SooHyung
"""

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        sum_divisers = num-1
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                sum_divisers -= (i + num//i)
        return sum_divisers == 0

'''
RESULT
Runtime 59ms, 22.1% beats
Memory 16.3MB, 33.67% beats
'''
