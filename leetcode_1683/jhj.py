# Write your MySQL query statement below
SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15

"""
Runtime: 1312 ms
Memory Usage: 0B
"""