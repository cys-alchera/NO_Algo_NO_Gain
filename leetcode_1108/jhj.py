class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")

"""
Runtime: 45 ms
Memory Usage: 16.2 MB
"""