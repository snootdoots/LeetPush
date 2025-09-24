class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        l, r = 0, 0
        curr_max = 0
        while r < len(s):
            # check if r+1 is in the set
            while s[r] in myset:
                myset.remove(s[l])
                l += 1
            myset.add(s[r])
            curr_max = max(curr_max, r-l+1)
            r += 1
        return curr_max