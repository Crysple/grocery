class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        
        cur_len = max_len = 1
        for i in range(len(A)):
            if i >= 2 and (A[i]>A[i-1]<A[i-2] or A[i]<A[i-1]>A[i-2]):
                cur_len += 1
            elif i >= 1 and A[i] != A[i-1]:
                cur_len = 2
            else: #A[i] == A[i-1] or i == 0
                cur_len = 1
            max_len = max(max_len, cur_len)
        return max_len
####################################################
        # Second though
        # if len(A) < 2:
        #     return len(A)
        # for i in range(len(A[:-1])):
        #     A[i] = -1 if A[i] > A[i+1] else int(A[i] < A[i+1])
        # cur_len = max_len = 1 if A[0] == 0 else 2
        # pos = 1
        # while pos < len(A) - 1:
        #     if A[pos] + A[pos-1] == 0 and A[pos] != 0:
        #         cur_len += 1
        #     else:
        #         max_len = max(max_len, cur_len)
        #         cur_len = 1 if A[pos] == 0 else 2
        #     pos += 1
        # return max(max_len, cur_len)
####################################################
        # First code
#         self.max_len = 0
#         self.start = self.end = 0
#         trend = 0 # 0 for init, 1 for upward and -1 for downward
        
#         def update_maxlen():
#             self.max_len = max(self.max_len, self.end-self.start+1)
#         def is_trend_right(trend):
#             a, b = A[self.end:self.end+2]
#             if trend==1: return a > b
#             return a < b
#         def get_trend():
#             return 1 if A[self.end] > A[self.end+1] else -1
#         def is_flat():
#             return A[self.end] == A[self.end+1]

#         for self.end in range(len(A)):
#             if self.end == len(A) - 1:
#                 update_maxlen()
#             elif trend == 0:
#                 if is_flat():
#                     update_maxlen()
#                     self.start = self.end + 1
#                 else:
#                     trend = get_trend()
#             elif not is_trend_right(trend): # end of turbulent
#                 update_maxlen()
#                 if is_flat():
#                     self.start = self.end + 1
#                     trend = 0
#                 else:
#                     self.start = self.end
#                     trend = get_trend()
#             trend = -trend
        
#         return self.max_len
