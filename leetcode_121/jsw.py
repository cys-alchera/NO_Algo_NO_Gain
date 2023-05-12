class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_buy_price = prices[0]
        
        for price in prices:
            if profit < price - min_buy_price:
                profit = price - min_buy_price

            if min_buy_price > price:
                min_buy_price = price
        
        return profit

# Runtime : 894ms, Beats : 99%
# Memory : 27.4MB, Beats : 14.87%
"""
--- 기존 코드로 Time Out이 발생 ---  리스트 인덱싱 슬라이싱에서 타임 아웃이 나는 걸로 생각
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_list = []
        if len(prices) == 1:
            return 0
        for buy_idx in range(len(prices)-1):
            buy_price = prices[buy_idx]
            sell_price = max(prices[buy_idx+1:])

            if sell_price > buy_price:
                profit_list.append(sell_price - buy_price)
            else:
                profit_list.append(0)
        
        return sorted(profit_list)[-1]
"""
