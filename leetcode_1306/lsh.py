"""
1306. Jump Game III
Lee SooHyung
"""

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        wasVisitList = [False]*len(arr)
        def jump(idx: int) -> bool:
            if idx < 0 or idx >= len(arr):
                return False
            if wasVisitList[idx]:
                return False
            if arr[idx] == 0:
                return True
            wasVisitList[idx] = True
            return jump(idx - arr[idx]) or jump(idx + arr[idx])
        return jump(start)

'''
RESULT
Runtime 317ms, 22.65% beats
Memory 73MB, 11.58% beats
'''

class Solution2:    # 보고 배운 코드
    def canReach(self, arr: List[int], start: int) -> bool:
                # visited가 List이면 TimeOut
        stack, visited, MAXLENGHT = [start], set(), len(arr)
        while stack:
            pos = stack.pop()
            if arr[pos] == 0:
                return True
            visited.add(pos)
            jumpRight, jupLeft = pos + arr[pos], pos - arr[pos]
            if jumpRight < MAXLENGHT and jumpRight not in visited:
                stack.append(jumpRight)
            if jupLeft >= 0 and jupLeft not in visited:
                stack.append(jupLeft)
        return False

'''
RESULT
Runtime 273ms, 99.66% beats
Memory 23.1MB, 64.18% beats
'''