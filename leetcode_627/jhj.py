# Write your MySQL query statement below
UPDATE Salary SET sex = CASE
    WHEN sex = 'f' THEN 'm'
    WHEN sex = 'm' THEN 'f'
END;

"""
Runtime: 632 ms
Memory Usage: 0B
"""