"""
2023-05-20
Leet Code 3
Longest Substring
Park Hee Chan
"""

def lengthOfLongestSubstring(s: str) -> int:
    # input string
    # longest repeat

    substring = ""
    memoization = list()
    if s == "":
        return 0
    if s == " ":
        return 1

    point = 1
    for c1 in s:
        substring = c1
        memoization.append(len(c1))
        for c2 in s[point:]:
            if c2 in substring:
                break

            print(substring, memoization)
            substring += c2
            memoization.append(len(substring))

        point += 1

    return max(memoization)

s = 'pwwkew'
print(lengthOfLongestSubstring(s))


'''
Runtime 558 ms
Beats 11.51%
Memory 39.7 MB
Beats 12.13%
'''
