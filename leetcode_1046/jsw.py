class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) > 1:
            stones.sort(reverse=True)
            weight_gap = stones[0] - stones[1]
            stones = stones[2:]
            stones.append(weight_gap)

            return self.lastStoneWeight(stones)

        if len(stones)==1:
            return stones[0]
        else:
            return 0  