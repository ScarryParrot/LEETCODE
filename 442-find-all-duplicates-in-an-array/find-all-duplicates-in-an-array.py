class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dict={}
        l=[]
        for i in nums:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        for i,c in dict.items():
            if c>1:
                l.append(i)
        return l