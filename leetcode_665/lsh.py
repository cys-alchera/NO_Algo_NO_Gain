"""
665. Non-decreasing Array
Lee SooHyung
"""

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        is_modify = False
        for idx in range(len(nums)-1):
            if nums[idx] <= nums[idx+1]:
                continue
            if is_modify:
                return False
            is_modify = True
            if idx==0 or nums[idx-1] <= nums[idx+1]:
                nums[idx] = nums[idx+1]
            else:
                nums[idx+1] = nums[idx]

        return True

'''
RESULT
Runtime 204ms, 13.17% beats
Memory 17.6MB, 26.73% beats
'''

'''
14 line과 15~18 line의 순서를 바꾸면 엄청나게 빨라짐.... 왜지?

        if idx==0 or nums[idx-1] <= nums[idx+1]:
            nums[idx] = nums[idx+1]
        else:
            nums[idx+1] = nums[idx]
        is_modify = True

RESULT
Runtime 176ms, 94.73% beats
Memory 17.8MB, 11.54% beats
'''