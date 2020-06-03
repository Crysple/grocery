class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # lower <= presum[hi] - presum[lo] <= upper
        # presum[hi] - upper <= presum[lo] <= presum[hi] - lower
        # lo < hi
        # a1, a2, a3,,,,a4, a5, a6
        # if ai >= a4 - upper, then aj >= a4 - upper for i<=j<=3,
        # if ak <= a4 - lower, then aj <= a4 - lower for 0<=j<=k,
        # so the number of satisfied number is max(0, k-i+1)
        presum = [0]
        for n in nums:
            presum.append(presum[-1]+n)
        arr = presum
        #arr = presum
        def merge_sort(l, r):
            # sort interval [l, r)
            if l >= r - 1: return 0
            mid = (l + r) // 2
            count = merge_sort(l, mid) + merge_sort(mid, r)
            result = []
            i = lid = hid = l
            for j in range(mid, r):
                while hid < mid and arr[j] - arr[hid] > upper:
                    hid += 1
                while lid < mid and arr[j] - arr[lid] >= lower:
                    lid += 1
                while i < mid and arr[j] > arr[i]:
                    result.append(arr[i])
                    i += 1
                count += lid - hid
                result.append(arr[j])
            result.extend(arr[i:mid])
            arr[l:r] = result
            return count
        return merge_sort(0, len(arr))
                    
