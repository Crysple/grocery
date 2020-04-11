class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        ans = 0
        start, end = 0, 1
        visited = {c:1 for c in p}
        while end < len(p) + 1:
            while end < len(p) and ord(p[end])-ord(p[end-1]) in [1, -25]:
                visited[p[end]] = max(visited[p[end]], end-start+1)
                end += 1
            start, end = end, end + 1
        return sum(visited.values())
