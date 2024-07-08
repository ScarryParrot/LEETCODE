class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(len(nums)-1,-1,-1):
            if sum(nums[:i]) < sum(nums[i:]):
                return reversed(nums[i:])