# https://leetcode.com/problems/search-insert-position/submissions/958278125/
# Runtime 56 msBeats56.16%Memory17.1 MBBeats 42.39%
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, enb = 0, len(nums) - 1
        
        while start <= enb:
            mid = (start + enb) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                start = mid + 1
            else:
                enb = mid - 1
        
        return start
