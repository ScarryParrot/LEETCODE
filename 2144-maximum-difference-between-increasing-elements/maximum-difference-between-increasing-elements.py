class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        k = float('inf')
        diff = -1

        for num in nums:
            if num > k:
                diff = max(diff, num - k)
            else:
                k = min(k, num)

        return diff