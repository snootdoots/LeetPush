class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        begin, end = strs[0], strs[len(strs)-1]
        ptr = 0
        while ptr < len(begin) and ptr < len(end) and begin[ptr] == end[ptr]:
            ptr += 1
        return begin[0:ptr]