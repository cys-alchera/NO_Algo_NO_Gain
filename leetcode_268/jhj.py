class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = len(nums)
        list_num = list(range(num+1))
        output = 0

        for i in list_num :
            if i not in nums :
                output = i
            else :
                continue
        
        return output