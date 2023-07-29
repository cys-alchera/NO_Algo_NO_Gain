# Write your MySQL query statement below
SELECT E2.employee_id, E2.name,
    COUNT(E1.employee_id) AS reports_count,
    ROUND(AVG(E1.age)) AS average_age 
FROM Employees E1 JOIN Employees E2 ON E1.reports_to = E2.employee_id
GROUP BY employee_id
ORDER BY employee_id

"""
Runtime: 1011 ms
Memory Usage: 0B
"""