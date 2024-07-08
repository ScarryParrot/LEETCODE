from typing import List
import bisect

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        arr = []
        n = len(nums)
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the first element
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue  # Skip duplicates for the second element
                for k in range(j + 1, n - 1):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue  # Skip duplicates for the third element
                    left_over = target - nums[i] - nums[j] - nums[k]
                    pos = bisect.bisect_left(nums, left_over, k + 1, n)
                    if pos < n and nums[pos] == left_over:
                        arr.append([nums[i], nums[j], nums[k], nums[pos]])
        return arr

