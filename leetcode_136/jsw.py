class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict = {}
        for num in nums:
            if num not in num_dict.keys():
                num_dict[num] = 1
            elif num_dict[num] >= 1:
                num_dict[num] += 1
            
        for key, item in num_dict.items():
            if item == 1:
                return key
            
"""
Runtime : 148 ms, Beats : 28.42%
Memory : 19.2 MB, Beats : 5.58%
"""