class Window:
    def __init__(self):
        self.counter = dict()
        self.n_distinct_num = 0

    def add(self, num):
        self.counter[num] = self.counter.get(num, 0) + 1
        if self.counter[num] == 1:
            self.n_distinct_num += 1

    def remove(self, num):
        self.counter[num] -= 1
        if self.counter[num] == 0:
            self.n_distinct_num -= 1

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        window1 = Window()
        window2 = Window()
        
        n_good_subarray = start1 = start2 = 0
        
        for end in range(len(A)):
            window1.add(A[end])
            window2.add(A[end])
            
            while window1.n_distinct_num > K:
                window1.remove(A[start1])
                start1 += 1
            
            while window2.n_distinct_num >= K:
                window2.remove(A[start2])
                start2 += 1
                
            n_good_subarray += start2 - start1

        return n_good_subarray
