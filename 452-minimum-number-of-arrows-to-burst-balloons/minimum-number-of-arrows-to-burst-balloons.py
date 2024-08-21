class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        c=1
        endl=points[0][1]
        for i in range(len(points)):
            if points[i][0] > endl:
                c+=1
                endl=points[i][1]
        return c
                