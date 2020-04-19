class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = list()
        waiting_days = [0] * len(T)
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                waiting_days[stack.pop()] = i - stack[-1]
            stack.append(i)
        return waiting_days
