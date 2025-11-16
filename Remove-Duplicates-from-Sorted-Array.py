class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 1
        curr_num = nums[0]
        while ptr < len(nums):
            if nums[ptr] == curr_num:
                if nums[ptr] == -101:
                    break
                nums.pop(ptr)
                nums.append(-101)
            else:
                curr_num = nums[ptr]
                ptr += 1
        
        while nums[-1] == -101:
            nums.pop()