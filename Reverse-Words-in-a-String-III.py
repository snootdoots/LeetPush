class Solution:
    def reverseWords(self, s: str) -> str:
        l, r = 0, len(s)-1
        returnstr = ""
        while l <= r:
            nextspace = l+1
            while nextspace < r+1 and s[nextspace] != ' ':
                nextspace += 1
            for i in range(nextspace-1, l-1, -1):
                returnstr += s[i]
            returnstr += ' '
            l = nextspace+1
        return returnstr.strip()