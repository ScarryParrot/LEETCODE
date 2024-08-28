class Solution:
    def findLongestChain(self, arr: List[List[int]]) -> int:
        # code here
        # arr1=[]
        c=0
        arr.sort(key=lambda x:x[1])
        end=arr[0][1]
        for i in range(1,len(arr)):
            if arr[i][0] > end:
                c+=1
                end=arr[i][1]
                # print(end)
        return c+1