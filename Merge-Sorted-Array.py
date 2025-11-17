class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums2)):
            nums1.pop()
        ptr = 0
        for num in nums2:
            while ptr < len(nums1) and num > nums1[ptr]:
                ptr += 1
            nums1.insert(ptr, num)