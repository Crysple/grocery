class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        nums = list(enumerate(nums))
        def mergesort(l, r):
            if l >= r - 1: return
            if l == r - 2:
                if nums[l][1] > nums[l+1][1]:
                    ans[nums[l][0]] += 1
                else:
                    nums[l], nums[l+1] = nums[l+1], nums[l]
                return
            mid = (l + r) // 2
            mergesort(l, mid)
            mergesort(mid, r)
            arr = []
            i, j = l, mid
            while i < mid and j < r:
                if nums[i][1] > nums[j][1]:
                    ans[nums[i][0]] += r - j
                    arr.append(nums[i])
                    i += 1
                else:
                    arr.append(nums[j])
                    j += 1
            arr += nums[i:mid] + nums[j:r]
            nums[l:r] = arr
        mergesort(0, len(nums))
        return ans
