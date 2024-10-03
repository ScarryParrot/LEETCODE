class Solution:
    def frequencySort(self, s: str) -> str:
        dict={}
        st=""
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]]+=1
            else:
                dict[s[i]]=1
        # print(dict)
        m=[]
        m.sort()
        m=m[::-1]
        for i,c in dict.items():
            m.append((i,c))
        m.sort(key=lambda x:x[1])
        m=m[::-1]
        for i,c in m:
            # print("i :  ",i)
            # print("c :  ",c)
            st+=str(c*i)
        return st

