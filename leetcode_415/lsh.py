"""
415. Add Strings
Lee SooHyung
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        lenNum1, lenNum2 = len(num1), len(num2)
        if lenNum1 > lenNum2:
            num2 = "0"*(lenNum1-lenNum2) + num2
        else:
            num1 = "0"*(lenNum2-lenNum1) + num1
        returnSum = ""
        flag = 0
        for idx in range(max(lenNum1, lenNum2)):
            sumNum = int(num1[-1-idx]) + int(num2[-1-idx]) + flag
            flag = sumNum // 10
            returnSum = str(sumNum % 10) + returnSum
        if flag:
            returnSum = str(flag) + returnSum
        return returnSum

'''
RESULT
Runtime 58ms, 21.86% beats
Memory 16.5MB, 12.34% beats
'''
