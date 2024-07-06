class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        c=0
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for num in freq:
            if k==0:
                if freq[num]>1:
                    c+=1
            else:
                if num+k in freq:
                    c+=1
        return c