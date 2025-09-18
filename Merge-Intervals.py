class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        idx = 0
        for i in intervals:
            intervals = sorted(intervals)
        while idx < len(intervals)-1:
            while idx < len(intervals)-1 and intervals[idx][1] >= intervals[idx+1][0]:
                intervals[idx][1] = max(intervals[idx][1], intervals[idx+1][1])
                intervals.pop(idx+1)
            idx += 1
        return intervals