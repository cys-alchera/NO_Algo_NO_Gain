"""
704 Binary Search
Lee SooHyung
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0, len(nums)
        while left < right-1:
            mid = left + (right-left)//2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            return left
        return -1

'''
RESULT
Runtime 247ms, 35.1% beats
Memory 17.7MB, 15.54% beats
'''

