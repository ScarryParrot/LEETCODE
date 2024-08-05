class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        prod=0
        while left < right:
            prod=max(prod,min(height[left],height[right])*(right-left))
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return prod