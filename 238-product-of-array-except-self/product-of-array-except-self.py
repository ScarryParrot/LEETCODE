class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre=1
        suff=1
        dp=[0]*n
        for i in range(n):
            dp[i]=pre
            pre*=nums[i]
        for i in range(n-1,-1,-1):
            dp[i] *=suff
            suff*=nums[i]
        return dp