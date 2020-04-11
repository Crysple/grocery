class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        wdlen, n_words = [*map(len, sentence)], len(sentence)
        ans = 0
        wid, rest_cols, rest_rows = 0, cols, rows-1
        pre_ans = pre_wid = 0
        dp = [False] * n_words
        while True:
            if wid >= n_words:
                ans += 1
                wid = 0
            if rest_cols == cols and dp[wid]:
                rest_rows -= 1
                ans += dp[wid][1]
                wid = dp[wid][0]
                if rest_rows < 0:
                    break
            elif wdlen[wid] > rest_cols:
                if rest_rows <= 0:
                    break
                dp[pre_wid] = (wid, ans - pre_ans)
                pre_wid, pre_ans = wid, ans
                rest_cols = cols
                rest_rows -= 1
            else:
                rest_cols -= wdlen[wid] + 1
                wid += 1
        return ans


