class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i] = 1
        for i,c in dict.items():
            if c ==1 :
                return i
        # return -1