class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = 0
        end = start = max_count = 0
        count = dict()
        while end < len(s):
            count[s[end]] = count.get(s[end], 0) + 1
            max_count = max(max_count, count[s[end]])
            if end - start + 1 - max_count > k:
                maxlen = max(maxlen, end-start)
                count[s[start]] -= 1
                start += 1
            end += 1
        return max(maxlen, end - start)
    
    # First thought
    # def characterReplacement(self, s: str, k: int) -> int:
    #     maxlen = 0
    #     for target in set(s):
    #         usedOp = 0
    #         i = j = 0
    #         while i < len(s):
    #             while i < len(s):
    #                 if s[i] == target:
    #                     i += 1
    #                     continue
    #                 # now s[i] != target
    #                 if usedOp == k:
    #                     break
    #                 usedOp += 1
    #                 i += 1
    #             maxlen = max(i-j, maxlen)
    #             while j < i:
    #                 if s[j] == target:
    #                     j += 1
    #                     continue
    #                 # s[j] != target
    #                 usedOp -= 1
    #                 j += 1
    #                 break
    #             # jump to next index that s[index] == target
    #             if usedOp == k:
    #                 while i < len(s) and s[i] != target:
    #                     i += 1
    #                 j = i
    #     return maxlen
                
                
