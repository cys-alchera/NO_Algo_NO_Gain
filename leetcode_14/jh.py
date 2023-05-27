# Runtime 49ms Beats 28.55% Memory 16.4MB Beats 24.85%

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_string = min(strs, key=len)

        for i ,char in enumerate(shortest_string):
            for str in strs:
                if str[i] != char:
                    return shortest_string[0:i]


        return shortest_string