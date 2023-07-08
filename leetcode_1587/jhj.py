SELECT Users.name, SUM(Transactions.amount) AS balance
FROM Users
RIGHT JOIN Transactions ON Users.account = Transactions.account
GROUP BY Users.name
HAVING SUM(Transactions.amount) > 10000;

"""
Runtime: 1609 ms
Memory Usage: 0B
"""