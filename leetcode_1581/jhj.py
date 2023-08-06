# Write your MySQL query statement below
SELECT customer_id,
    COUNT(V.customer_id) AS count_no_trans
From Visits AS V
LEFT JOIN Transactions T ON V.visit_id = T.visit_id
WHERE T.visit_id is Null
GROUP BY customer_id

"""
Runtime: 3226 ms
Memory Usage: 0B
"""