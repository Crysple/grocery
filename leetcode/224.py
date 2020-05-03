class Solution:
    def calculate(self, s: str) -> int:
        s = "(" + s + ")"
        stack = []
        sign = 1
        n = level_res = 0
        for c in s:
            if c.isnumeric():
                n = n * 10 + int(c)
            elif c in "+-":
                level_res += n * sign
                sign = 1 if c == "+" else -1
                n = 0
            elif c == "(":
                stack += [level_res, sign]
                sign, level_res = 1, 0
            elif c == ")":
                level_res += n * sign
                level_res *= stack.pop() # add sign
                level_res += stack.pop()
                n = 0
        return level_res + n * sign
