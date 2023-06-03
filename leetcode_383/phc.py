"""
230603
383. Ransom Note
Hash Table
Park Hee Chan
https://leetcode.com/problems/ransom-note/
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mem = dict()
        for letter in ransomNote:
            if letter not in mem.keys():
                mem[letter] = 1
                continue
            mem[letter] += 1

        for letter in magazine:
            if letter in mem.keys():
                mem[letter] -= 1

        print(mem)
        for key, value in mem.items():
            if value > 0:
                return False

        return True


'''
Runtime 94 ms
Beats 19.55%

Memory 16.6 MB
Beats 38.28%
'''