class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        c = 0
        freq = {}
        
        for num in nums:
            if num - k in freq:
                c += freq[num - k]
            if num + k in freq:
                c += freq[num + k]
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
                
        return c
