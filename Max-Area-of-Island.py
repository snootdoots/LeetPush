class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def dfs(r,c):
            if r<=-1 or c<=-1 or c>=len(grid[0]) or r>=len(grid) or visited[r][c] or grid[r][c]==0:
                return 0
            visited[r][c] = True
            mysum = 1
            for x,y in [(0,1), (1,0), (0,-1), (-1,0)]:
                mysum += dfs(r+x,c+y)
            return mysum

        curr_max = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1 and not visited[x][y]:
                    curr_max = max(curr_max, dfs(x,y))
        return curr_max