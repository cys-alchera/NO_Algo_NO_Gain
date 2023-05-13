"""
2023.05.13
Number of Islands
PARK HEE CHAN
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # grid [ [], [], [], [] ]
        # 4 x 5
        # 1 == land
        # 0 == water
        # 1 <= m, n <= 300

        # m = grid.length
        # n = grid.length

        # check 4 directional.. 4 floor check?
        count = 0
        m = len(grid)

        def recursive_check(grid, m, n, r, c):
            if (r < 0 or r > m - 1) or (c < 0 or c > n - 1) or grid[r][c] == "0":
                return

            print(r, c)
            grid[r][c] = "0"
            recursive_check(grid, m, n, r - 1, c)
            recursive_check(grid, m, n, r + 1, c)
            recursive_check(grid, m, n, r, c + 1)
            recursive_check(grid, m, n, r, c - 1)

        for r in range(m):
            n = len(grid[r])

            for c in range(n):
                print(f"{r + 1}/{m},  {c + 1}/{n}")
                target = grid[r][c]
                if target == "1":
                    recursive_check(grid, m, n, r, c)
                    count += 1

        return count


'''
recursive and clear island's values.

Runtime
451 ms

Beats
5.63%

Memory
19 MB

Beats
40.28%
'''