"""
1865. Finding Pairs With a Certain Sum
Lee SooHyung
"""

from collections import Counter
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = Counter(nums1)
        self.nums2 = Counter(nums2)
        self.nums2_List = nums2

    def add(self, index: int, val: int) -> None:
        self.nums2[self.nums2_List[index]] -= 1
        self.nums2_List[index] += val
        self.nums2[self.nums2_List[index]] += 1

    def count(self, tot: int) -> int:
        resultCount = 0
        for num in self.nums1:
            if tot - num in self.nums2:
                resultCount += self.nums2[tot - num] * self.nums1[num]
        return resultCount


'''
RESULT
Runtime 672ms, 97.76% beats
Memory 49MB, 18.66% beats
'''
