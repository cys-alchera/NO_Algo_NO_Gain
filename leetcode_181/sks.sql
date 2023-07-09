SELECT name as Employee FROM Employee e1 WHERE salary > (SELECT salary from Employee where id = e1.managerId)

-- Runtime 1598ms Beats 8.54%
