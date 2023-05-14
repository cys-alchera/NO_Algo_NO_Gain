class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for _ in range(len(nums)):
            if nums[pointer] == 0:
                nums.append(nums.pop(pointer))
            else:
                pointer += 1

"""
Runtime : 172ms, Beats : 51.77%
Memory : 17.9MB, Beats : 15.50%
"""