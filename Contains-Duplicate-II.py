class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myset = set()
        for i in range(min(k+1, len(nums))):
            if nums[i] in myset:
                return True
            myset.add(nums[i])
        for i in range(1, len(nums)):
            myset.remove(nums[i-1])
            if i+k < len(nums):
                if nums[i+k] in myset:
                    return True
            if i+k < len(nums):
                myset.add(nums[i+k])
        return False