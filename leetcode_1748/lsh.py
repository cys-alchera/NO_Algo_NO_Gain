"""
1748. Sum of Unique Elements
Lee SooHyung
"""

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        output = 0
        nonUniqueNums = {}
        for num in nums:
            if num in nonUniqueNums:
                if nonUniqueNums[num] == 1:
                    output -= num
                nonUniqueNums[num] += 1
            else:
                output += num
                nonUniqueNums[num] = 1
        return output

'''
RESULT
Runtime 47ms, 24.12% beats
Memory 16.4MB, 5.62% beats
'''
