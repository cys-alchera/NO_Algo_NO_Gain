"""
1507. Reformat Date
Lee SooHyung
"""

class Solution:
    def reformatDate(self, date: str) -> str:
        Month_table = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        day, month, year = date.split(" ")
        return f"{year}-{Month_table[month]}-{day[:-2].zfill(2)}"


'''
RESULT
Runtime 40ms, 78.66% beats
Memory 16.3MB, 66.80% beats
'''
