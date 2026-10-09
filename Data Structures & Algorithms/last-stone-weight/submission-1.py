class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        
        for i in stones:
            heapq.heappush(pq, -i) # push [-1,-2]
        while(len(pq) > 1):
            x = heapq.heappop(pq) # x = -2
            y = heapq.heappop(pq) # y = -1
            if x < y:
                heapq.heappush(pq, x-y) # -2 + 1 = -1
        if len(pq) == 0:
            return 0
        return -(pq[0])
