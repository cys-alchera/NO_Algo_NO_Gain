"""
1640. Check Array Formation Through
Lee SooHyung
"""

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        hashTable = {x[0]:x for x in pieces}
        idx = 0
        while idx < len(arr):
            if arr[idx] in hashTable and arr[idx:idx+len(hashTable[arr[idx]])] == hashTable[arr[idx]]:
                idx += len(hashTable[arr[idx]])
            else:
                return False
        return True

'''
RESULT
Runtime 47ms, 61.33% beats
Memory 16.3MB, 14.33% beats
'''
