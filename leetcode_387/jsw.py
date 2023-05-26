from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_counter = Counter(s)

        for key in char_counter:
            if char_counter[key] == 1:
                return s.find(key)
        return -1

        # char_dict = {}
        # for idx, char in enumerate(s):
        #     if char not in char_dict:
        #         char_dict[char] = [idx]
        #     else:
        #         char_dict[char].append(idx)
        
        # for key, value in char_dict.items():
        #     if len(value) == 1:
        #         return value[0]
        # return -1