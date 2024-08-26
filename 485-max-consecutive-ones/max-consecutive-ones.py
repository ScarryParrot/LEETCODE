class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        d=0
        for i in nums:
            if i == 1:
                c+=1
            else:
                d=max(c,d)
                c=0
        
        c=max(c,d)
        return c