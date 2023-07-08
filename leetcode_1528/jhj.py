class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = [0] * len(s)
        for s, idx in zip(s, indices):
            output[idx] = s

        return ''.join(output)

"""
Runtime: 61 ms
Memory Usage: 16.4 MB
"""