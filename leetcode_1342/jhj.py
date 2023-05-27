class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0

        while num > 0 :
            if num % 2 == 0 :
                num = num // 2
                step += 1
                continue
            
            else :
                num -= 1
                step += 1
        
        return step

"""
Runtime: 46 ms
Memory Usage: 16.2 MB
"""