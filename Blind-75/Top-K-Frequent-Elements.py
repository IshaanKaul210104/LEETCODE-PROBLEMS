class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        m = Counter(nums)

        for val, freq in m.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, val))
            else:
                if freq > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (freq, val))

        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])

        return ans
