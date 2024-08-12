class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        for i in range(0,n+1):
            if i not in nums:
                c=i
        return c