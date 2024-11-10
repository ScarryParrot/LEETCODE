class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dict={}
        for i in nums:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        a=[]
        m=max(dict.values())
        for i,c in dict.items():
            if c == m:
                a.append(c)
        return (len(a)*a[0])
