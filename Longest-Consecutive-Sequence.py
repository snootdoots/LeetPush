class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        currmax = 0
        for num in myset:
            if num-1 not in myset:
                curr = num
                # start of chain
                currlen = 1
                while curr+1 in myset:
                    currlen += 1
                    curr += 1
                currmax = max(currlen, currmax)
        return currmax