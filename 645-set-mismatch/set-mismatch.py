from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count_dict = {}
        result = []
        
        # Step 1: Populate the count_dict with occurrences of each number
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                count_dict[num] += 1
        
        # Step 2: Identify the duplicated number and the missing number
        duplicated = -1
        missing = -1
        n = len(nums)
        
        for i in range(1, n + 1):
            if i not in count_dict:
                missing = i
            elif count_dict[i] == 2:
                duplicated = i
        
        return [duplicated, missing]
