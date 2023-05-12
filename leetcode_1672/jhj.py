class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum_list = []
        for account in accounts :
            sum_list.append(sum(account))

        return max(sum_list)

"""
Runtime: 75 ms
Memory Usage: 16.4 MB
"""