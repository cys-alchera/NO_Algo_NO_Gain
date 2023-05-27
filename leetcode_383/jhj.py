class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        setsransomNote = set(ransomNote)
        magazine = list(magazine)

        total = 0

        for item in setsransomNote:
            if item in magazine:
                num1 = ransomNote.count(item)
                num2 = magazine.count(item)
                if num2 >= num1:
                    total += 1
            else :
                return False
        
        if total == len(setsransomNote):
            return True

"""
Runtime: 86 ms
Memory Usage: 16.7 MB
"""