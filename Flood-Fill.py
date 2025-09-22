class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def bfs(image, sr, sc, curr, val):
            image[sr][sc] = val
            visited = [[False for i in range(len(image[0]))] for j in range(len(image))]
            queue = [(sr, sc)]
            while queue:
                x, y = queue.pop(0)
                # north
                if y-1 >= 0 and image[x][y-1] == curr and not visited[x][y-1]:
                    queue.append((x, y-1))
                    image[x][y-1] = val
                    visited[x][y-1] = True
                # south
                if y+1 < len(image[x]) and image[x][y+1] == curr and not visited[x][y+1]:
                    queue.append((x, y+1))
                    image[x][y+1] = val
                    visited[x][y+1] = True
                # east
                if x+1 < len(image) and image[x+1][y] == curr and not visited[x+1][y]:
                    queue.append((x+1, y))
                    image[x+1][y] = val
                    visited[x+1][y] = True
                # west
                if x-1 >= 0 and image[x-1][y] == curr and not visited[x-1][y]:
                    queue.append((x-1, y))
                    image[x-1][y] = val
                    visited[x-1][y] = True
            return image

        image = bfs(image, sr, sc, image[sr][sc], color)
        return image
                