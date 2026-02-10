from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r - 1):
            for j in range(i + 1, c):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(r):
            matrix[i].reverse()
        return matrix

print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))