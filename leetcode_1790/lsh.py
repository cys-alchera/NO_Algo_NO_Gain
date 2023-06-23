"""
1790. Check if One String Swap Can Make Strings Equal
Lee SooHyung
"""

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        diff = [i for i in range(len(s1)) if s1[i] != s2[i]]

        return len(diff) == 2 and s1[diff[0]] == s2[diff[1]] and s1[diff[1]] == s2[diff[0]]

'''
RESULT
Runtime 48ms, 49.44% beats
Memory 16.4MB, 25.23% beats
'''
