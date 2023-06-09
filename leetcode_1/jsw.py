class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
"""
Runtime 3844 ms
Beats 26.92%
Memory 17.2 MB
Beats 56.53%
"""
