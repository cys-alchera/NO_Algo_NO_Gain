class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join(list(map(lambda x: x[:-1], sorted(s.split(' '), key = lambda x: x[-1])))) 
    
"""
Runtime 46 ms
Beats 39.71%

Memory 16.4 MB
Beats 17.7%
"""