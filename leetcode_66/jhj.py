class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int(''.join(map(str, digits)))
        number += 1
        number = list(map(int, str(number)))
        return number

"""
Runtime: 46 ms
Memory Usage: 16.2 MB
"""