# https://leetcode.com/problems/surrounded-regions/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        N = len(board)
        M = len(board[0])

        for i in range(N):
            for j in range(M):
                if board[i][j] == "O":
