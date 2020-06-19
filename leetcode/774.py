class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        def count(dis):
            cnt = 0
            for i in range(1, len(stations)):
                if stations[i] - stations[i-1] > dis:
                    cnt += math.ceil((stations[i] - stations[i-1]) / dis) - 1
                    if cnt > K:
                        break
            return cnt
        l, r = 0, max([j - i for i, j in zip(stations, stations[1:])]) + 1
        while r - l > (10e-6):
            mid = l + (r - l) / 2
            needed = count(mid)
            #print(l, r, needed)
            if needed <= K:
                r = mid
            else:
                l = mid
        return l
