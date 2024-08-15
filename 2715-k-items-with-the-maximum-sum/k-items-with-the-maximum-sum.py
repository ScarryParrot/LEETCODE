class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        c=0
        return min(numOnes,k)-max(0,min(numNegOnes,max(0,k-(numOnes+numZeros))))
        