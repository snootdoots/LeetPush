class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) >= 2 and nums[1] < nums[0] or len(nums) == 1:
            return 0
        if len(nums) >= 2 and nums[len(nums)-2] < nums[len(nums)-1]:
            return len(nums)-1
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i