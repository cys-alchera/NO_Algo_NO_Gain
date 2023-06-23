"""
2600. K Items With the Maximum Sum
Lee SooHyung
"""

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes >= k:
            return k
        elif numOnes + numZeros >= k:
            return numOnes
        else:
            return numOnes - (k - (numOnes + numZeros))
        

'''
RESULT
Runtime 42ms, 71.61% beats
Memory 16.3MB, 53.42% beats
'''
