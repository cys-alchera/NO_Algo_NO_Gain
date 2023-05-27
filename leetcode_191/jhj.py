class Solution:
    def hammingWeight(self, n: int) -> int:
        n_list = list(bin(n)[2:])
        num_1bits = n_list.count("1")

        return num_1bits

"""
Runtime: 46 ms
Memory Usage: 16.1 MB
"""