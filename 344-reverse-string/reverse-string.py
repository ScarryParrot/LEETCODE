class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        arr=[]
        for i in range(len(s)):
            arr.append(s.pop())
        s.extend(arr)
        