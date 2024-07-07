from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = 1
        zero_count = 0
        
        for num in nums:
            if num==0:
                zero_count+=1
            else:
                prod*=num
        arr=[]
        if zero_count >1:
            return [0]*n
        for num in nums:
            if zero_count==0:
                arr.append(prod//num)
            else:
                if num ==0:
                    arr.append(prod)
                else:
                    arr.append(0)
        return arr