class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def mutate(s1, s2):
            # assume that len(s1) == len(s2)
            if not sorted(s1) == sorted(s2):
                return False
            if len(s1) < 4 or s1 == s2:
                return True
            for i in range(1, len(s1)):
                if (mutate(s1[:i], s2[-i:]) and mutate(s1[i:], s2[:-i])
                    or mutate(s1[:i], s2[:i]) and mutate(s1[i:], s2[i:])):
                    return True
            return False
        if len(s1) != len(s2):
            return False
        return mutate(s1, s2)
