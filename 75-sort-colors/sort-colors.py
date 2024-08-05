class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero,one,n=0,0,len(nums)
        for num in nums:
            if num==0:
                zero+=1
            if num==1:
                one+=1
        for i in range(0,zero):
            nums[i]=0
        
        for i in range(zero,zero+one):
            nums[i]=1
        
        for i in range(zero+one,n):
            nums[i]=2        