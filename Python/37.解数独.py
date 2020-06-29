#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
class Solution:
    # def solveSudoku(self, board: List[List[str]]) -> None:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def find_available_num(board, i, j):
            avilable_nums = '123456789'
            for num in board[i]:
                avilable_nums = avilable_nums.replace(num, '')
            for line in board:
                avilable_nums = avilable_nums.replace(line[j], '')
            for a in range(i//3*3, i//3*3+3):
                for b in range(j//3*3, j//3*3+3):
                    avilable_nums = avilable_nums.replace(board[a][b], '')
            return avilable_nums

        def next_num(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        avilable_nums = find_available_num(board, i, j)
                        if avilable_nums:
                            for avilable_num in avilable_nums:
                                board[i][j] = avilable_num
                                print(i, j)
                                print(avilable_num)
                                print(board)
                                next_num(board)
                        break
        
        next_num(board)
        print(board)

if __name__ == "__main__":
    s = Solution()
    s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])

