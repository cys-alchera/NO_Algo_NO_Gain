"""
2427. Number of Common Factors
Lee SooHyung
"""

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        small, big = min(a,b), max(a,b)
        count = 0
        for i in range(1, small+1):
            if i > small/i:
                break
            if small%i==0 and big%i==0:
                count += 1
                if i == small/i:
                    break
            if small%i==0 and big%(small//i)==0:
                count += 1
        return count

'''
RESULT
Runtime 32ms, 73.74% beats
Memory 16.2MB, 14.87% beats
'''
