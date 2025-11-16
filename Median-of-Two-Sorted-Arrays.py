class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # naive solution :/
        res = []
        ptr1, ptr2 = 0, 0
        while ptr1 < len(nums1) or ptr2 < len(nums2):
            if ptr1 < len(nums1) and ptr2 < len(nums2):
                if nums1[ptr1] <= nums2[ptr2]:
                    res.append(nums1[ptr1])
                    ptr1 += 1
                else:
                    res.append(nums2[ptr2])
                    ptr2 += 1
            elif ptr1 < len(nums1):
                res.extend(nums1[ptr1:])
                ptr1 = len(nums1)
            else:
                res.extend(nums2[ptr2:])
                ptr2 = len(nums2)

        if len(res) % 2 == 0:
            mid = len(res) // 2
            return (res[mid-1] + res[mid]) / 2
        else:
            mid = len(res) // 2
            return res[mid]