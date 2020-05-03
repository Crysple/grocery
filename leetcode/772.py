class Solution:
    def calculate(self, s: str) -> int:
        def cal(op, a, b):
            if op == "+": return a + b
            elif op == "-": return a - b
            elif op == "*": return a * b
            else: return a // b
        stack = [] # store level status with the following 5 variables
        addsub, muldiv, preop, res, term = "+", "*", "+", 0, 1
        n = 0
        for c in s+"+0":
            if c.isnumeric():
                n = n * 10 + int(c)
            elif c in "+-":
                if preop in "*/":
                    n = cal(preop, term, n)
                    term, muldiv = 1, "*"
                res = cal(addsub, res, n)
                n = 0
                addsub = preop = c
            elif c in "*/":
                term = cal(muldiv, term, n)
                n = 0
                muldiv = preop = c
            elif c == ")":
                if preop in "*/":
                    n = cal(preop, term, n)
                    term, muldiv = 1, "*"
                # get value of () and assign to n, treated as a new number
                n = cal(addsub, res, n)
                # restore status of upper level
                addsub, muldiv, preop, res, term = stack[-5:]
                stack = stack[:-5]
            elif c == "(":
                stack.extend([addsub, muldiv, preop, res, term])
                addsub, muldiv, preop, res, term = "+", "*", "+", 0, 1
        return res
