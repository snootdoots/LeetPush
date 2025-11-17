class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        top = 0 
        top_val = 0
        for i, v in ctr.items():
            if v > top_val:
                top = i
                top_val = v
        return top