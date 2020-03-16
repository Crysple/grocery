from collections import Counter
class Window:
    def __init__(self, target_string):
        self.need = Counter(target_string)
        self.n_need = len(self.need)

    def remove(self, x):
        self.need[x] += 1
        if self.need[x] == 1:
            self.n_need += 1

    def add(self, x):
        self.need[x] -= 1
        if self.need[x] == 0:
            self.n_need -= 1

    def satisfied(self):
        return self.n_need == 0


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = Window(t)

        start = end = 0
        minlen = len(s) + 1
        minstr = ""
        for end in range(len(s)):
            window.add(s[end])
            while window.satisfied():
                if minlen > end - start + 1:
                    minlen = end - start + 1
                    minstr = s[start:end+1]
                window.remove(s[start])
                start += 1
        return minstr
