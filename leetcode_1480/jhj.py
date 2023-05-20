class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        input_list = []
        sum_list = []
        for num in nums :
            input_list.append(num)
            sum_list.append(sum(input_list))
    
        return sum_list
    
"""
Runtime: 65 ms
Memory Usage: 16.6 MB
"""