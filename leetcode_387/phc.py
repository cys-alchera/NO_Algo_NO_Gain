"""
230603
387. First Unique Character in a String
Hash Table
Park Hee Chan
https://leetcode.com/problems/first-unique-character-in-a-string/
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:

        mem = dict()

        for i, letter in enumerate(s):
            if letter in mem.keys():
                mem[letter]['count'] += 1
            if letter not in mem.keys():
                mem[letter] = dict(first_index=i, count=1)

        state = False
        guess = len(s)
        print(mem)
        for key in mem.keys():
            if mem[key]['count'] == 1:
                guess = min(mem[key]['first_index'], guess)
                state = True

        if state:
            return guess
        return -1

'''
Runtime 224 ms
Beats 20.98%

Memory 16.8 MB
Beats 12.48%
'''
