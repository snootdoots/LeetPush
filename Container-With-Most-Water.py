class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        curr_max = (r-l) * min(height[l], height[r])
        while l < r:
            if height[l] >= height[r]: # greedily decrement right if equal
                r -= 1
            else:
                l += 1
            curr_max = max(curr_max, (r-l) * min(height[l], height[r]))
        return curr_max
            