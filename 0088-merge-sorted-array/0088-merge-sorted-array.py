class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        count = 0
        res = m+n
        while m<res:
            nums1[m] = nums2[count]
            count+=1
            m+=1
        for i in range(len(nums1)):
            for j in range(0, len(nums1)-i-1):
                if nums1[j] > nums1[j + 1]:
                    temp = nums1[j]
                    nums1[j] = nums1[j+1]
                    nums1[j+1] = temp
        
        