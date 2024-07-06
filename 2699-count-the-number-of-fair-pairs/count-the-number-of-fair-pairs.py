class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        c=0
        for i in range(len(nums)):
            low_bound=bisect_left(nums,lower-nums[i],i+1)
            higher_bound=bisect_right(nums,upper-nums[i],i+1)-1
            c+=max(0,higher_bound-low_bound+1)
        return c