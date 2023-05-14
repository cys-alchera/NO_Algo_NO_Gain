"""
844 Backspace String Compare
Lee SooHyung
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.refineString(s) == self.refineString(t)

    def refineString(self, string: str):
        result_string = []
        for c in string:
            if c != "#":
                result_string.append(c)
            elif result_string:
                result_string.pop()
        return "".join(result_string)

'''
RESULT
Runtime 49ms, 9.9% beats
Memory 16.4MB, 15.49% beats
'''
