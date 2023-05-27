ROMAN = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000             
        }
# Runtime 53ms Beats 63.62% Memory 16.3MB Beats 14.90%
class Solution:
    def romanToInt(self, s: str) -> int:
        i = len(s) - 1
        integer = 0
        last_num = 0
        while i >= 0:
            current = ROMAN[s[i]]
            if last_num <= current:
                integer += current
            else:
                integer -= current
            last_num = current
            i -= 1
        return integer
    