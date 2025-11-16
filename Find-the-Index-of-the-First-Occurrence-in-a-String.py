class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        letter = needle[0]
        ptr = 0
        while ptr < len(haystack):
            if haystack[ptr] == letter:
                if haystack[ptr:ptr+len(needle)] == needle:
                    return ptr
            ptr += 1
        return -1