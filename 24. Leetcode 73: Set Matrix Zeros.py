from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        row_track = [0] * r
        col_track = [0] * c
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    matrix[i][j] = float("-inf")
                    row_track[i] = -1
                    col_track[j] = -1

        for i in range(len(row_track)):
            for j in range(len(col_track)):
                if col_track[j] == -1 or row_track[i] == -1:
                    matrix[i][j] = 0
        return matrix

print(Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]]))