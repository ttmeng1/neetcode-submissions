class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix)
        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            # mid = columns(current row) + current column
            val = matrix[mid // cols][mid % cols]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False