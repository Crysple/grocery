class Window:
    def __init__(self, max_cost):
        self.resource = max_cost

    def get_cost(self, s, t):
        return abs(ord(s) - ord(t))

    def add(self, s, t):
        cost = self.get_cost(s, t)
        if cost <= self.resource:
            self.resource -= cost
            return True
        return False

    def remove(self, s, t):
        self.resource += self.get_cost(s, t)
        
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        window = Window(maxCost)
        
        start = end = maxlen = 0
        for end in range(len(s)):
            while not window.add(s[end], t[end]):
                maxlen = max(maxlen, end-start)
                window.remove(s[start], t[start])
                start += 1

        return max(maxlen, end-start+1)
