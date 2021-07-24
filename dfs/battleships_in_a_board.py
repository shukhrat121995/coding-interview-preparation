"""
Given an m x n matrix board where each cell is a battleship 'X' or empty '.',
return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the
shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal
or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2

Input: board = [["."]]
Output: 0

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is either '.' or 'X'.

Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?
"""


class Solution:
    def countBattleshipsBestSolution(self, board: list[list[str]]) -> int:
        num_of_ships = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if board[i][j] == '.': continue
                    if i > 0 and board[i - 1][j] == 'X': continue
                    if j > 0 and board[i][j - 1] == 'X': continue
                    num_of_ships += 1

        return num_of_ships

    def countBattleshipsSimpleSolution(self, board: list[list[str]]) -> int:
        num_of_ships = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    num_of_ships += 1
                    self.dfs(board, i, j)

        return num_of_ships

    def dfs(self, board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] != 'X':
            return

        board[i][j] = '.'

        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j + 1)
        self.dfs(board, i, j - 1)
