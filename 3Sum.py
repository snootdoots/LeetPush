class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        soln = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            k = -nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[l] + nums[r]
                if s == k:
                    soln.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif s < k:
                    l += 1
                else:
                    r -= 1
        return soln
                