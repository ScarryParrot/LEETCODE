class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[]
        for i in nums1 :
            found=False
            for j in range(len(nums2)):
                if i == nums2[j]:
                    for k in range(j+1,len(nums2)):
                        if i < nums2[k]:
                            found = True
                            arr.append(nums2[k])
                            break
                    if found:break
            if not found: arr.append(-1)
        return arr