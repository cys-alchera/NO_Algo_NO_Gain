# Write your MySQL query statement below
SELECT a1.machine_id, ROUND(AVG(a2.timestamp - a1.timestamp),3) as processing_time
FROM Activity a1
JOIN Activity a2
on a1.process_id=a2.process_id
and a1.machine_id=a2.machine_id
and a1.timestamp < a2.timestamp
group by a1.machine_id

"""
Runtime: 478 ms
Memory Usage: 0B
"""