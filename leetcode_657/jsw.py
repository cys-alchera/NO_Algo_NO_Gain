class Solution:
    def judgeCircle(self, moves: str) -> bool:
        direction = {'U' : 1, 'D' : -1, 'L' : -1, 'R' : 1}
        offset = [0,0]

        for move in moves:
            if (move == 'U') or (move == 'D'):
                offset[0] += direction[move]
            else:
                 offset[1] += direction[move]
        return True if offset == [0,0] else False