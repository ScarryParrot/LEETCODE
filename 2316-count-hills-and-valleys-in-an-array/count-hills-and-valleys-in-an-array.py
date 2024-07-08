class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        c = 0
        
        # Clean up the input by removing consecutive duplicates
        cleaned_nums = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                cleaned_nums.append(nums[i])
        
        # Count hills and valleys in the cleaned list
        for i in range(1, len(cleaned_nums) - 1):
            if cleaned_nums[i] > cleaned_nums[i - 1] and cleaned_nums[i] > cleaned_nums[i + 1]:
                c += 1
            elif cleaned_nums[i] < cleaned_nums[i - 1] and cleaned_nums[i] < cleaned_nums[i + 1]:
                c += 1
                
        return c