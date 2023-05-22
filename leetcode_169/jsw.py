from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter_dict = Counter(nums)
        threshold = len(nums) / 2

        for key, values in counter_dict.items():
            if values > threshold:
                return key
        