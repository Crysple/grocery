class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        # Using a stack: O(n)
        stack = []
        curr = 0
        for c in S:
            if c == '(':
                stack.append(curr)
                curr = 0
            else:
                curr = max(curr*2, 1)
                curr += stack.pop() if stack else 0
        return curr
        # Divide and Conquer: O(n^2)
        def bt(i, end):
            j = i
            score = left = 0
            while j < end:
                left += 1 if S[j]=='(' else -1
                if left == 0:
                    score += (bt(i+1, j) * 2) if i < j - 1 else 1
                    i = j + 1
                j += 1
            return score
        return bt(0, len(S))
