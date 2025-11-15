class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ptr1, ptr2 = 0, 0
        end1, end2 = len(nums1), len(nums2)
        while ptr1 < end1 and ptr2 < end2 and nums1[ptr1] != nums2[ptr2]:
            if nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            else:
                ptr2 += 1
        if ptr1 == end1 or ptr2 == end2:
            return -1
        return nums1[ptr1]