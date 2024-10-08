class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        # print(nums)
        arr=[]
        for i,c in enumerate(nums):
            if c == target:
                arr.append(i)
        return arr 