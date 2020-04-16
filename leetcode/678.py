class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        star = left = match_left = potential_left = 0
        for c in s:
            if c == '(':
                left += 1
            elif c == '*':
                if left > 0:
                    left -= 1
                    match_left +=1
                else:
                    star += 1
            # now c == ')'
            elif left <= 0 and star <= 0 and potential_left <= 0 and match_left <= 0:
                return 0
            elif left > 0:
                left -= 1
            elif potential_left > 0:
                potential_left -= 1
            elif star > 0:
                star -= 1
            else:
                match_left -= 1
                potential_left += 1
        return left == 0
