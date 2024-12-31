class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols  # Initialize heights array
        max_area = 0

        for i in range(rows):
            # Update heights array for the current row
            for j in range(cols):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Compute the largest rectangle in the current histogram
            stack = []
            for idx, h in enumerate(heights + [0]):  # Add a sentinel to handle the last bar
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = idx if not stack else idx - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(idx)

        return max_area