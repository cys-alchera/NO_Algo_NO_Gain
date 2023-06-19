class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0

        for a,b in zip(heights, expected):
            if a != b:
                count += 1
        return count