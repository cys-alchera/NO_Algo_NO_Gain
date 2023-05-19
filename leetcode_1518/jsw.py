class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int: 
        betray_bottles = numBottles
        while betray_bottles >= numExchange:
            numBottles += betray_bottles // numExchange
            betray_bottles = betray_bottles // numExchange + betray_bottles % numExchange
        
        return numBottles