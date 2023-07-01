class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_nums = {}
        set_nums = list(set(nums))
        
        for i in set_nums :
            dict_nums[i] = nums.count(i)
        
        output = [k for k, v in dict_nums.items() if v == 1]
        return output[0]

"""
Runtime: 4765 ms
Memory Usage: 19.8 MB
"""