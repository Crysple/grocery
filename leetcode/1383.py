import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        worker = sorted(zip(efficiency, speed), reverse=True)
        total_speed = performace = 0
        speeds = []
        for idx, (efficiency, speed) in enumerate(worker):
            if idx >= k:
                total_speed -= heapq.heappop(speeds)
            total_speed += speed
            heapq.heappush(speeds, speed)
            performace = max(performace, total_speed * efficiency)
        return performace % (10**9+7)
