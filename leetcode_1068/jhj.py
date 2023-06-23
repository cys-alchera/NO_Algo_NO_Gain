# Write your MySQL query statement below
SELECT Product.product_name, Sales.year, Sales.price
FROM Sales
LEFT JOIN Product ON Sales.product_id = Product.product_id

"""
Runtime: 2441 ms
Memory Usage: 0B
"""