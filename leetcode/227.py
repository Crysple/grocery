class Solution:
    def calculate(self, s: str) -> int:
        # only use simple op
        addsub = pre_op = "+" # previous op
        muldiv = "*"
        res = n = 0
        term = 1
        for c in s+"+0":
            if c.isnumeric():
                n = n * 10 + int(c)
            elif c in "+-":
                if pre_op in "*/":
                    n = (term * n) if muldiv == "*" else (term // n)
                    term, muldiv = 1, "*"
                res = (res + n) if addsub == "+" else (res - n)
                addsub = pre_op = c
                n = 0
            elif c in "*/":
                term = (term * n) if muldiv == "*" else (term // n)
                muldiv = pre_op = c
                n = 0
        return res
        # Using Regular expression
        import re
        ans = 0
        outer = iter(["+"] + re.split('([+-])', s))
        for addsub in outer:
            cur = 1
            inner = iter(["*"] + re.split('([*/])', next(outer)))
            for muldiv in inner:
                if muldiv == "*":
                    cur *= int(next(inner))
                elif muldiv == "/":
                    cur //= int(next(inner))
            ans = (ans + cur) if addsub == "+" else (ans - cur)
        return ans
