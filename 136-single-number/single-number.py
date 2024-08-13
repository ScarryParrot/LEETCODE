from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_dict = {}
        
        # Count occurrences of each number
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                count_dict[num] += 1
        
        # Find the number that occurs exactly once
        for num, count in count_dict.items():
            if count == 1:
                return num
