"""
2023.05.13
Park Hee Chan
backspaceCompare
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        if self.backspace_apply(list(s)) == self.backspace_apply(list(t)):
            return True
        return False

    def backspace_apply(self, target: list):
        result = list()
        for txt in target:
            if txt == '#':
                if result:
                    result.pop()
                continue
            result.append(txt)

        return "".join(result)


'''
Runtime 57 ms
Beats 6.47%

Memory 16.4 MB
Beats 15.49%
'''