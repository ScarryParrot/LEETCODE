class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}  # Dictionary to store the numbers and their indices
        
        for i in range(len(nums)):
            diff = target - nums[i]
            
            # Check if the current number's complement (diff) is in the dictionary
            if nums[i] in dict:
                return [dict[nums[i]], i]  # Return the stored index and current index
            
            # Otherwise, store the current number's complement and its index in the dictionary
            dict[diff] = i
