class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i,c in enumerate(nums):
            diff=target-c
            if c in dict:
                return [dict[c],i]
            else:
                dict[diff]=i
        return []