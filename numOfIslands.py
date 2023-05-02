"""
Given an m x n 2D binary grid grid which represnets a map of 1s (land) and 0s (water), return the
number of islands
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically
You may assume all four edges of the grid are all surrounded by water.
"""

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    """
    We use depth first search (DFS), iterate over each cell in the grid, and if the cell
    contains an 1, we mark it as visited, and recursively explore all of its adjacent cells
    that contain a 1
    
    we use a separate function to perform the dfs search on each unvisited land cell, and increment
    a counter every time we start a new DFS search
    The counter represents the number of islands in the grid
    """
    def dfs(grid, i, j):
      #if the current cell is out of bounds or contains a 0, we return.
      if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
        return
      #otherwise we mark the current cell as visited by setting its value as 0, and recursively
      #call dfs on all of its adjacent cells that contain a 1.
      grid[i][j] = "0"
      dfs(grid, i+1, j)
      dfs(grid, i-1, j)
      dfs(grid, i, j+1)
      dfs(grid, i, j-1)
    
    #we then initializea a counter to 0 and iterate over each c ell in the grid using two nested for loops
    count = 0
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        #if the current cell contains a 1, we increment the counter and call DFS on the current cell
        #to explore all of its adjacent land cells
        if grid[i][j] == "1":
          count += 1
          dfs(grid, i, j)
    #finally we return the counter count which represents the number of islands in the grid
    #this algorithm has a time complexity of O(m*n), where m and n are the dimensions of the grid,
    #since we visit each cell in the grid at most once.
    return count
