class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        i = j = 0
        slots1 = sorted(slots1, key=lambda x: x[0])
        slots2 = sorted(slots2, key=lambda x: x[0])
        def get_overlap(a, b):
            overlap = min(a[1], b[1]) - max(a[0], b[0])
            return max(overlap, 0)
        while i < len(slots1) and j < len(slots2):
            if get_overlap(slots1[i], slots2[j]) >= duration:
                start = max(slots1[i][0], slots2[j][0])
                return [start, start + duration]
            if slots1[i][1] > slots2[j][1]:
                j += 1
            else:
                i += 1
        return []
