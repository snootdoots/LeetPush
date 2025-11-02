class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1
        
        pq = []
        for key, val in counts.items():
            heapq.heappush(pq, (val, key))
            if len(pq) > k:
                heapq.heappop(pq)
        
        return [key for (val, key) in pq]