"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if matrix is None:
            return []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        res = list()

        while top <= bottom and left <= right:
            # ---------> right, constant: top
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # ---------> down, constant: right
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # ---------> left, constant: bottom
            if top <= bottom:  # check row still exists
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            # ---------> up, constant: left
            if left <= right:  # check column still exists
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res


