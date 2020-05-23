class Solution:
    def minWindow(self, S: str, T: str) -> str:
        # idea borrow from solution
        # instead of length, use index as the value of dp
        # Plus, use a dict (c: [ids] in T) to optimize the second loop
        dp = [0] * (len(T)+1)
        min_len = float('inf')
        alpha = collections.defaultdict(list)
        for i, c in enumerate(T):
            alpha[c].append(i+1)
        for k in alpha:
            alpha[k] = alpha[k][::-1]
        for i in range(1, len(S)+1):
            for j in alpha[S[i-1]]:
                if S[i-1] == T[j-1]:
                    if j == 1: dp[j] = i
                    else: dp[j] = dp[j-1]
            #print(S[i-1], dp)
            if dp[-1] and i - dp[-1] + 1 < min_len:
                min_len = i - dp[-1] + 1
                end = i
        if min_len != float('inf'):
            return S[end-min_len:end]
        return ""

        # My original answer: O(NM) without optimization
        # dp[i, j] means the length of the window such that window[-1] is S[i] and T[j]
        # if S[i] == T[j]: dp[i, j] = dp[i-1, j-1] + 1
        # else: dp[i, j] = dp[i-1, j]
        dp = [0] * (len(T)+1)
        min_len = float('inf')
        for i in range(1, len(S)+1):
            ndp = [0] * (len(T)+1)
            for j in range(1, len(T)+1):
                if S[i-1] == T[j-1]:
                    if dp[j-1] or j == 1:
                        ndp[j] = dp[j-1] + 1
                else:
                    ndp[j] = dp[j] + (1 if dp[j] else 0)
            #print(S[i-1], ndp)
            if ndp[-1] and ndp[-1] < min_len:
                #print(min_len, i-1)
                min_len = ndp[-1]
                end = i
            dp = ndp
        if min_len != float('inf'):
            return S[end-min_len:end]
        return ""
        
