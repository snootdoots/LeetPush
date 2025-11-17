class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        best = 0
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            best = max(best, w*h)

            # move pointers
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                if height[l+1] > height[r-1]:
                    l += 1
                else:
                    r -= 1
        return best