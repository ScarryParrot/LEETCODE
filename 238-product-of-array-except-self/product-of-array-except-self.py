from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = 1
        zero_count = 0
        
        # Calculate the product of all non-zero elements and count zeros
        for num in nums:
            if num != 0:
                prod *= num
            else:
                zero_count += 1
        
        # If more than one zero, all products will be zero
        if zero_count > 1:
            return [0] * n
        
        arr = []
        for num in nums:
            if zero_count == 0:
                arr.append(prod // num)
            else:
                if num == 0:
                    arr.append(prod)
                else:
                    arr.append(0)
        
        return arr
