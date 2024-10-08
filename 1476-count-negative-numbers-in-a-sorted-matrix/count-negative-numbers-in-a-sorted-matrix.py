class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        a=0
        for i in grid:
            for j in i:
                if j <0 :
                    a+=1
        return a