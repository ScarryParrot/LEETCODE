class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums:
            return None
        first=second=float('inf')
        for n in nums:
            if first >=n:
                first=n
            elif second >= n:
                second=n
            else:
                return True
        return False