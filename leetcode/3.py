class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lengthOfLongestSubstring = 0
        headOfWindow = 0
        window = dict()

        def removeCharFromWindow(char):
            '''Remove char from window by one'''
            window[char] -= 1
            if window[char] == 0:
                del window[char]

        def moveForwardHead(begin, char):
            '''Shrinking the window by moving forward the head of window'''
            while s[begin] != char:
                removeCharFromWindow(s[begin])
                begin += 1
            removeCharFromWindow(s[begin])
            return begin + 1

        for idx, char in enumerate(s):
            if char in window:
                headOfWindow = moveForwardHead(headOfWindow, char)
            window[char] = window.get(char, 0) + 1
            lengthOfLongestSubstring = max(lengthOfLongestSubstring, idx-headOfWindow+1)

        return lengthOfLongestSubstring
