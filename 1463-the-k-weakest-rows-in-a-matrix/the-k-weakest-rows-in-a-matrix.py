class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dict={}
        for i in range(len(mat)):
            one=0
            for j in mat[i]:
                if j == 1:
                    one+=1
            # print(one)
            dict[i]=one
        arr=[]
        # print(dict)
        sr = sorted(dict.items(), key=lambda x: (x[1], x[0]))
        # print(sr)
        for i,c in sr[:k]:
            arr.append(i)
            print("c  :  ",c)
        return arr