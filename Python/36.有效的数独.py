#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkValid(checking_board):
            while '.' in checking_board:
                checking_board.remove('.')
            return len(checking_board) == len(set(checking_board))

        for i in range(9):
            if not checkValid([b[i] for b in board]):
                return False
            tmp = board[i].copy()
            if not checkValid(tmp):
                return False
            if not checkValid([board[i//3*3+j//3][i*3%9+j%3] for j in range(9)]):
                return False
        return True
# @lc code=end
