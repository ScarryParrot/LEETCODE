class Solution:
    def replaceDigits(self, s: str) -> str:
        st=""
        left,right=0,1
        while right < len(s):
            st+=s[left]
            # st+=chr(ord(s[left])+s[right])
            st+=chr(int(ord(s[left]))+int(s[right]))
            left+=2
            right+=2
        if s[-1].isdigit():
            pass
        else:
            st+=s[-1]
        return st
