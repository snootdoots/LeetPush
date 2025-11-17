class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search to find one element
        guess = -1
        l, r = 0, len(nums)
        while l < r:
            m = (l+r)//2
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m
            else:
                guess = m
                break
        if guess == -1:
            return [-1, -1]
        
        l, r = m, m
        while l > 0:
            if nums[l-1] == target:
                l -= 1
            else:
                break
        while r < len(nums)-1:
            if nums[r+1] == target:
                r += 1
            else:
                break
        return [l, r]