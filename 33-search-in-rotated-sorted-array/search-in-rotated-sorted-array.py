class Solution:
    def search(self, nums: List[int], t: int) -> int:
        low,high=0,len(nums)-1
        while low <= high:
            mid = low+ (high-low)//2
            if t == nums[mid]:
                return mid
            if nums[low] <= nums[mid] : 
                if nums[low] <= t < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid] < t <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1