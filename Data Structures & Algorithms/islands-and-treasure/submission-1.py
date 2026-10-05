from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        
        m, n = len(grid), len(grid[0])

        # Directions for moving up, down, left, and right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Depth-First Search function
        def dfs(x, y, distance):
            # If the current distance is greater than or equal to the cell's current value, stop
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] < distance:
                return
            
            # Update the grid cell with the current shortest distance
            grid[x][y] = distance
            
            # Explore all 4 directions
            for dx, dy in directions:
                dfs(x + dx, y + dy, distance + 1)

        # Start DFS from each treasure chest (0) in the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    # Perform DFS for each treasure cell with an initial distance of 0
                    dfs(i, j, 0)

        # No need to return anything as the grid is updated in-place
