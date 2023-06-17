# Write your MySQL query statement below
SELECT * FROM Cinema
WHERE id % 2 != 0 AND description <> 'boring'
ORDER BY rating DESC;

"""
Runtime: 506 ms
Memory Usage: 0B
"""