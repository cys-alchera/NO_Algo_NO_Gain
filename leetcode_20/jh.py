# https://leetcode.com/problems/valid-parentheses/description/
# Runtime 37 ms Beats 53.78% Memory 16.4 MB Beats 17.60%
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        bracket_close_open_pair = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        if len(s) % 2 == 1:
            return False
        
        stack = []
        for index, char in enumerate(s):
            if self.is_open_type(bracket_close_open_pair, char):
                stack.append(char)
            elif len(stack) == 0 or not self.is_pair(bracket_close_open_pair, stack.pop(), char):
                return False

            if len(s) - index < len(stack):
                return False
        return len(stack) == 0

    def is_pair(self, bracket_pair: dict, open_char: str, close_char: str) -> bool:
        return bracket_pair[close_char] == open_char

    def is_close_type(self, bracket_pair: dict, s: str) -> bool:
        return s in bracket_pair
    
    def is_open_type(self, bracket_pair: dict, s: str) -> bool:
        return not self.is_close_type(bracket_pair, s)
    