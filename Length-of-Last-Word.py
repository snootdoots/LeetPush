class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ptr = len(s)-1
        while ptr > 0 and not s[ptr].isalpha():
            ptr -= 1
        if ptr < 0:
            return 0
        ctr = 0
        while ptr >= 0 and s[ptr].isalpha():
            ptr -= 1
            ctr += 1
        return ctr