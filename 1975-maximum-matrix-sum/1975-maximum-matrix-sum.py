from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        neg_count = 0
        min_abs = float('inf')

        for row in matrix:
            for val in row:
                total_sum += abs(val)
                if val < 0:
                    neg_count += 1
                min_abs = min(min_abs, abs(val))

        if neg_count % 2 == 1:
            total_sum -= 2 * min_abs

        return total_sum

        