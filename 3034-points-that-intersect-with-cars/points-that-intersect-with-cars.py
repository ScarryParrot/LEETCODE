class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        p=set()
        for i in nums:
            for n in range(i[0],i[1]+1):
                p.add(n)
        return len(p)