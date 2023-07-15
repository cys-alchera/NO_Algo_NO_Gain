class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        result = ''
        for word in s:
            for idx in range(1, len(word)+1):
                result += word[-idx]
            result += ' '
        return result.strip()
