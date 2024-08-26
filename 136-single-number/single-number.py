class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict={}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]]=1
            else:
                dict[nums[i]]+=1
        print(dict)
        for i,c in dict.items():
            if c == 1:
                return i