class Solution:
    def strStr(self, hay: str, needle: str) -> int:
        c=0
        if needle in hay:
            for i in range(len(hay)):
                if hay[i:len(needle)+i] == needle:
                    return i
        else: return -1