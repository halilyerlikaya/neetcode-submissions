from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        
        m, n = len(grid), len(grid[0])
        queue = deque()

        # Add all treasure cells (cells with 0) to the queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        # Directions for moving up, down, left, and right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Perform BFS
        while queue:
            x, y = queue.popleft()

            # Check all 4 possible directions
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                # Check if new cell is within bounds and is an unvisited land cell (INF)
                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 2147483647:
                    # Update the distance for the new cell
                    grid[new_x][new_y] = grid[x][y] + 1
                    # Add the new cell to the queue
                    queue.append((new_x, new_y))

        # No need to return anything since grid is updated in-place.
