class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        pre_sum = [0]
        for cp in cardPoints:
            pre_sum.append(pre_sum[-1] + cp)
        ans = 0
        for i in range(k+1):
            ans = max(ans, pre_sum[i]+ (pre_sum[-1] - pre_sum[-(k-i)-1]))
        return ans
