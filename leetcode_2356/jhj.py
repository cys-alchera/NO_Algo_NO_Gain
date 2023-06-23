# Write your MySQL query statement below
SELECT teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id

"""
Runtime: 1036 ms
Memory Usage: 0B
"""