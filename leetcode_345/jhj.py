class Solution:
    def reverseVowels(self, s: str) -> str:
        import numpy as np

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels_index = []
        vowels_values = []

        list_s = list(s)
        print(list_s)

        for i in vowels :
            if i in s:
                pos = np.where(np.array(list_s) == i)[0]
                vowels_index.append(pos)

        if len(vowels_index) > 1:
            vowels_index = np.concatenate(vowels_index).tolist()
            vowels_index = sorted(vowels_index)
        else :
            return s

        for i in vowels_index :
            vowels_values.append(list_s[i])

        vowels_values.reverse()

        for i in range(len(vowels_index)):
            idx = vowels_index[i]
            list_s[idx] = vowels_values[i]

        return ''.join(list_s)

"""
Runtime: 323 ms
Memory Usage: 36 MB
"""