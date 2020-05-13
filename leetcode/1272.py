class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []
        for intv in intervals:
            if intv[0] < toBeRemoved[0]:
                if toBeRemoved[0] >= intv[1]:
                    ans.append(intv)
                else:
                    ans.append([intv[0], toBeRemoved[0]])
                    if intv[1] > toBeRemoved[1]:
                        ans.append([toBeRemoved[1], intv[1]])
            elif toBeRemoved[0] <= intv[0] <= toBeRemoved[1]:
                if intv[1] > toBeRemoved[1]:
                    ans.append([toBeRemoved[1], intv[1]])
            else:
                ans.append(intv)
        return sorted(ans, key=lambda x:x[0])
