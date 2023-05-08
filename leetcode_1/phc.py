"""
200509 TWO SUM Problem
Park Hee Chan
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mem = 0
        idx_list = list()
        for i in range(len(nums)):
            data = target - nums[i]
            if data in nums[i+1:]:
                idx_list.append(i)
                mem = data
                continue
            if nums[i] == mem:
                idx_list.append(i)

        return idx_list

"""
Runtime 647ms, 40.27% beats
Memory 17MB, 16.50% beats
"""

