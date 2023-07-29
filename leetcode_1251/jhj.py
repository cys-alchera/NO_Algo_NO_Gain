SELECT P.product_id, ROUND(SUM(U.units * P.price) / SUM(U.units),2) AS average_price
FROM Prices AS P
JOIN UnitsSold AS U 
on P.product_id = U.product_id AND (U.purchase_date BETWEEN P.start_date AND P.end_date)
GROUP BY product_id

"""
Runtime: 2298 ms
Memory Usage: 0B
"""