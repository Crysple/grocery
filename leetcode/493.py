class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(l, r, arr):
            # sort interval [l, r)
            if l >= r - 1: return 0
            mid = (l + r) // 2
            count = merge_sort(l, mid, arr) + merge_sort(mid, r, arr)
            result = []
            i = tid = l
            # count arr[tid] > 2 * arr[j]
            for j in range(mid, r):
                while tid < mid and arr[tid] <= 2 * arr[j]:
                    tid += 1
                while i < mid and arr[j] > arr[i]:
                    result.append(arr[i])
                    i += 1
                count += mid - tid
                result.append(arr[j])
            result.extend(arr[i:mid])
            arr[l:r] = result
            return count
        #print(pos, neg, ans)
        return merge_sort(0, len(nums), nums)
