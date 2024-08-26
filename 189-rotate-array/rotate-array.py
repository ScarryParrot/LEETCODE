from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(l: int, r: int) -> None:
            """
            Helper function to reverse elements in nums from index l to r.
            """
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        n = len(nums)
        k = k % n  # Handle cases where k >= n

        # Reverse the entire list
        rev(0, n - 1)
        # Reverse the first k elements
        rev(0, k - 1)
        # Reverse the remaining n - k elements
        rev(k, n - 1)
