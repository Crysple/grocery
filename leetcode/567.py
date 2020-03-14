from collections import Counter
#import re
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        start = end = 0
        while end < len(s2):
            counter[s2[end]] -= 1
            while counter[s2[end]] < 0:
                counter[s2[start]] += 1
                start += 1
            if end - start + 1 == len(s1):
                return True
            end += 1
        return False
        
        
        # First thought
        # then https://leetcode.com/problems/permutation-in-string/discuss/102590/8-lines-slide-window-solution-in-Java
#         useless_chars = ''.join(set(s2) - set(s1))
#         if useless_chars:
#             possible_substrs = re.split("[{}]".format(useless_chars), s2)
#         else:
#             possible_substrs = [s2]

#         for s in possible_substrs:
#             start = end = 0
#             waiting_char, need = len(set(s1)), Counter(s1)
#             while end < len(s):
#                 endchar = s[end]
#                 # get repeat char, move start pointer
#                 if need[endchar] == 0:
#                     while s[start] != endchar:
#                         if need[s[start]] == 0:
#                             waiting_char += 1
#                         need[s[start]] += 1
#                         start += 1
#                     # now s2[start] == endchar == s2[end]
#                     start += 1
#                 else:
#                     need[endchar] -= 1
#                     # finish one character
#                     if need[endchar] == 0:
#                         waiting_char -= 1
#                         if waiting_char == 0:
#                             return True
#                     #####
#                 end += 1
#         return False
