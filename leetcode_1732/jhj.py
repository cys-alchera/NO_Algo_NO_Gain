class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = []
        altitudes.append(0)

        for i in range(len(gain)):
            sum_alt = altitudes[i] + gain[i]
            altitudes.append(sum_alt)
        
        if max(altitudes) <=0 :
            return 0
        
        else :
            return max(altitudes)

"""
Runtime: 50 ms
Memory Usage: 16.4 MB
"""