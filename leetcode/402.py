class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        K = k
        for i, c in enumerate(num):
            while stack and num[stack[-1]] > c and k:
                k -= 1
                stack.pop()
            stack.append(i)
            if k == 0:
                break
        res = (''.join([num[i] for i in stack]) + num[stack[-1]+1:])[:len(num)-K].lstrip('0')
        return res if res else '0'
            
