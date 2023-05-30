"""
447. Number of Boomerangs
Lee SooHyung
"""

from collections import defaultdict
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def calcDistance(point1, point2):
            return (((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**0.5)

        count = 0
        for i in points:
            distTable = defaultdict(int)
            for j in points:
                distTable[calcDistance(i, j)] += 1
            for dist in distTable:
                count += distTable[dist] * (distTable[dist]-1)

        return count

'''
RESULT
Runtime 1722ms, 16.30% beats
Memory 16.6MB, 45.11% beats
'''
