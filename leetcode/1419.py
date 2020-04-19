class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        sound = "croak"
        count = {c:0 for c in sound}
        ans = -1
        for char in croakOfFrogs:
            if char not in count:
                return -1
            count[char] += 1
            for c in sound:
                if count[c] < count[char]:
                    return -1
                if c == char:
                    break
            ans = max(ans, max(count.values()))
            if c == 'k':
                for i in count:
                    count[i] -= 1
            
        if len(set(count.values())) == 1:
            return ans
        return -1
