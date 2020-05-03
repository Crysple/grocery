import re
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def cal(op, a, b):
            if op == "*": return a * b
            if op == "-": return a - b
            return a + b
        expr = re.split("([-+*])", input)
        #print(expr)
        expr[::2] = [int(n) for n in expr[::2]]
        @lru_cache(None)
        def waysToComput(lo, hi):
            if lo == hi - 1:
                return (expr[lo],)
            ways = []
            for idx in range(lo+1, hi, 2):
                op = expr[idx]
                left = waysToComput(lo, idx)
                right = waysToComput(idx+1, hi)
                for lans in left:
                    for rans in right:
                        ways.append(cal(op, lans, rans))
            return tuple(ways)
        return waysToComput(0, len(expr))
