class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) < len(word2):
            max_len = len(word2)
            word1 = list(word1) + [""] * (max_len - len(word1))
            word2 = list(word2)
        else:
            max_len = len(word1)
            word2 = list(word2) + [""] * (max_len - len(word2))
            word1 = list(word1)

        total_word = ""
        for i in range(max_len) :
            total_word += word1[i]+word2[i]

        return total_word

"""
Runtime: 51 ms
Memory Usage: 16.5 MB
"""