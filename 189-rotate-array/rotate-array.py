from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # To handle cases where k >= n
        dp = [0] * n

        # Populate the dp array with rotated values
        for i in range(n):
            dp[(i + k) % n] = nums[i]
        
        # Copy the dp array back to nums
        for i in range(n):
            nums[i] = dp[i]
