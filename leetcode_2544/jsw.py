class Solution:
    def alternateDigitSum(self, n: int) -> int:
        result = 0
        for idx in range(len(str(n))):
            if idx % 2 == 0:
                result += eval(str(n)[idx])
            else:
                result -= eval(str(n)[idx])
        return result