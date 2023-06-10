"""
162. Find Peak Element
Lee SooHyung
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid

        return l

'''
RESULT
Runtime 66ms, 21.11% beats
Memory 16.3MB, 74.83% beats
'''
