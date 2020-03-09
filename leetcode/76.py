from collections import Counter
class Window:
    def __init__(self, string, neededChars):
        self.string = string
        self.neededChars = neededChars
        self.head = self.tail = self.nSatisfiedChar = 0

    def isLegal(self):
        return self.nSatisfiedChar == len(self.neededChars)
    
    def reachEnd(self):
        return self.head == len(self.string)

    def getLength(self):
        return self.head - self.tail + 1

    def moveHead(self):
        '''move head forward one step'''
        char = self.string[self.head]
        if char in self.neededChars:
            self.neededChars[char] -= 1
            if self.neededChars[char] == 0:
                self.nSatisfiedChar += 1
        self.head += 1

    def moveTail(self):
        '''move tail forward'''
        char = self.string[self.tail]
        if char in self.neededChars:
            if self.neededChars[char] == 0:
                self.nSatisfiedChar -= 1
            self.neededChars[char] += 1
        self.tail += 1

    def shrinkToIllegal(self):
        while self.isLegal():
            self.moveTail()

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = Window(s, Counter(t))

        tailOfMinWindow = -1
        minLengthOfWindow = len(s) + 1

        def updateMinWindow(window, minLengthOfWindow, tailOfMinWindow):
            curLength = window.getLength()
            if curLength < minLengthOfWindow:
                minLengthOfWindow = curLength
                tailOfMinWindow = window.tail - 1
            return minLengthOfWindow, tailOfMinWindow

        while True:
            window.moveHead()
            if window.isLegal():
                window.shrinkToIllegal()
                minLengthOfWindow, tailOfMinWindow = updateMinWindow(window, minLengthOfWindow, tailOfMinWindow)
            if window.reachEnd():
                break
            
        if tailOfMinWindow != -1:
            return s[tailOfMinWindow:tailOfMinWindow+minLengthOfWindow]
        return ""
