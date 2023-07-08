class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()','o').replace('(al)','al')

"""
Runtime: 37 ms
Memory Usage: 16.3 MB
"""