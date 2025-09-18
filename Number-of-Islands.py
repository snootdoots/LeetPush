class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # double for loop through 1s and 0s graph
        # create a mxn visited graph
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        count = 0

        def dfs(x, y, grid, visited):
            # we only call dfs if grid[x][y] == 1
            stack = []
            stack.append((x, y))
            while stack:
                x, y = stack.pop()
                visited[x][y] = True
                # N
                if y-1 >= 0 and grid[x][y-1] == '1' and not visited[x][y-1]:
                    stack.append((x, y-1))
                # E
                if x+1 < len(grid) and grid[x+1][y] == '1' and not visited[x+1][y]:
                    stack.append((x+1, y))
                # S
                if y+1 < len(grid[x]) and grid[x][y+1] == '1' and not visited[x][y+1]:
                    stack.append((x, y+1))
                # W
                if x-1 >= 0 and grid[x-1][y] == '1' and not visited[x-1][y]:
                    stack.append((x-1, y))

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == '1':
                    if visited[x][y]:
                        pass
                    else:
                        dfs(x, y, grid, visited)
                        count += 1
        return count