from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_dict = {}
        arr = []
        zero_count = 0

        # Count occurrences of each number
        for i in nums:
            if i == 0:
                zero_count += 1
            else:
                if i in count_dict:
                    count_dict[i] += 1
                else:
                    count_dict[i] = 1
        
        # Build the `arr` list with non-zero elements in original order
        for num in nums:
            if num != 0:
                arr.append(num)
        
        # Append zeros at the end
        arr.extend([0] * zero_count)
        
        # Modify `nums` in-place
        for i in range(len(nums)):
            nums[i] = arr[i]
