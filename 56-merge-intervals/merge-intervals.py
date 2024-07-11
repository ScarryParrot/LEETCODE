class Solution:
    def merge(intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[intervals[0]]
        for i in range(1,len(intervals)):
            if ans[-1][1]>=intervals[i][0]:
                if intervals[i][1]>ans[-1][1]:
                    ans[-1][1]=intervals[i][1]
            else:
                ans.append(intervals[i])
        print(ans)

    sys.stdout=open('user.out','w')
    for i in map(loads,stdin):
        merge(i)
    exit()