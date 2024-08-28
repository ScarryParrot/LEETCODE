class Solution:
    def isAnagram(self,s,t):
        if len(s) != len(t):
            return False
        dict={}
        for i in s:
            if i not in dict:
                dict[i] =1
            else:
                dict[i] +=1
        for i in t:
            if i in dict:
                dict[i] -=1
        for i,c in dict.items():
            if c !=0 :
                return False
        return True