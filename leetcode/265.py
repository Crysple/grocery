class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        def getMin(house):
            if len(house) <= 2:
                return house[::-1]
            forwardmin = house[:1]
            for c in house[1:]:
                forwardmin += min(c, forwardmin[-1]),
            curmin = house[-1]
            forwardmin[-1] = forwardmin[-2]
            for cid in range(len(house)-2, -1, -1):
                forwardmin[cid] = min(forwardmin[cid-1], curmin) if cid>0 else curmin
                curmin = min(house[cid], curmin)
            return forwardmin
        if not costs:
            return 0
        prehouse = getMin(costs[0])
        for house in costs[1:]:
            for cid in range(len(house)):
                house[cid] += prehouse[cid]
            prehouse = getMin(house)
        return min(prehouse)
