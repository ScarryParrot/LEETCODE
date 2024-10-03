class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        left, right = 0, 1
        sums = {}
        
        while right < len(nums):
            subarray_sum = nums[left] + nums[right]
            if subarray_sum in sums:
                return True  # If the sum is already in the dictionary, return True (duplicate found)
            sums[subarray_sum] = True  # Store the sum in the dictionary
            left += 1
            right += 1
        
        return False  # If no duplicate sum is found, return False
