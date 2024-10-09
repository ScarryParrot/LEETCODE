from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            
            # Ensure `mid` is even for correct pair checking
            if mid % 2 == 1:
                mid -= 1
            
            # If the pair is valid, move `low` to `mid + 2`
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid
        
        # `low` will point to the single element
        return nums[low]
