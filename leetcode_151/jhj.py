class Solution:
    def reverseWords(self, s: str) -> str:
        s = [i for i in s.split(" ") if i != '']
        
        sentence = ""
        for i in reversed(s) :
            sentence += i
            sentence += " "
        
        return sentence[:-1]

"""
Runtime: 56 ms
Memory Usage: 16.6 MB
"""    
        


