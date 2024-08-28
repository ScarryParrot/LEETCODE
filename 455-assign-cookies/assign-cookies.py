class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  # Sort greed factors
        s.sort()  # Sort cookie sizes

        child = 0  # Index for greed factor
        cookie = 0  # Index for cookies

        # Iterate until we run out of either children or cookies
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:  # If the cookie can satisfy the child
                child += 1  # Move to the next child
            cookie += 1  # Move to the next cookie

        return child  # Number of content children
