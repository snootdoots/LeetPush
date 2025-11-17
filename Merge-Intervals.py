class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ptr = 0
        while ptr < len(intervals)-1:
            curr = intervals[ptr]
            begin, end = curr[0], curr[1]
            nxt = intervals[ptr+1]
            nbegin, nend = nxt[0], nxt[1]
            if nbegin <= end:
                intervals[ptr][0] = min(begin, nbegin)
                intervals[ptr][1] = max(end, nend)
                intervals.pop(ptr+1)
            else:
                ptr += 1

        return intervals