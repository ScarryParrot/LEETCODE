class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end=intervals[0][1]
        c=0
        for i in range(1,len(intervals)):
            if intervals[i][0] < end:
                c+=1
            else:
                end=intervals[i][1]
        return c