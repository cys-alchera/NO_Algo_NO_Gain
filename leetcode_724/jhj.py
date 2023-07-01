class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for pivot in range(len(nums)):
            left = sum(nums[:pivot])
            right = sum(nums[pivot+1:])

            if left == right:
                return pivot
        
        return -1

"""
Runtime: 8841 ms
Memory Usage: 17.5 MB
"""