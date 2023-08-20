# Write your MySQL query statement below
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(*) > 4

"""
Runtime: 591 ms
Memory Usage: 0B
"""