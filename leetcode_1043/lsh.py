"""
1043. Partition Array for Maximum Sum
Lee SooHyung
"""

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        afterArr = [0] * (len(arr)+1)

        for idx in range(1, len(arr)+1):
            subArrMax = 0
            for subIdx in range(1, min(idx, k)+1):
                subArrMax = max(subArrMax, arr[idx-subIdx])
                afterArr[idx] = max(afterArr[idx], afterArr[idx-subIdx] + subArrMax*(subIdx))
        return afterArr[-1]

     
'''
RESULT
Runtime 445ms, 89.29% beats
Memory 16.4MB, 38.20% beats
'''
