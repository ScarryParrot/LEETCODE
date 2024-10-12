class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 0 or n == 0:
            return False
        def po(x):
            prod=1
            prod=pow(3,x)
            if prod == n:
                return True
            if prod > n:
                return False
            return po(x+1)
        return po(0)