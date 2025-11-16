class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        pq = []
        for item, count in counter.items():
            heapq.heappush(pq, (-count, item))
        out = []
        for _ in range(k):
            count, item = heapq.heappop(pq)
            out.append(item)
        return out