class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort() 
        l = 0
        r = len(nums1)
        m = int((l + r) / 2)
        rtype = 0.0
        if r % 2 == 0:
            rtype = (nums1[m-1]+nums1[m]) / 2.0
            return rtype
        elif r % 2 == 1:
            rtype = nums1[m]
            return rtype

nums1 = [1,2]
nums2 = [3,4]
s = Solution()
rv = s.findMedianSortedArrays(nums1,nums2)
print(rv)
