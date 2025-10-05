from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev_height):
            if (
                r < 0 or c < 0 or r >= m or c >= n or
                (r, c) in visited or heights[r][c] < prev_height
            ):
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # Start from the borders touching the Pacific and Atlantic
        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])       # Pacific (left)
            dfs(i, n - 1, atlantic, heights[i][n - 1])  # Atlantic (right)
        for j in range(n):
            dfs(0, j, pacific, heights[0][j])       # Pacific (top)
            dfs(m - 1, j, atlantic, heights[m - 1][j])  # Atlantic (bottom)

        # Cells reachable by both oceans
        result = list(pacific & atlantic)
        return result
