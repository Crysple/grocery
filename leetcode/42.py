class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] <= h:
                mid = stack.pop()
                if stack:
                    water += (min(h, height[stack[-1]]) - height[mid]) * (i - stack[-1] - 1)
            stack.append(i)
        return water
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         i, j = 0, len(height) - 1
#         volumn = 0
#         while i < j:
#             if height[i] < height[j]:
#                 prev = height[i]
#                 i += 1
#                 while i < j and height[i] < height[j]:
#                     if prev - height[i] > 0:
#                         volumn += prev - height[i]
#                     else:
#                         prev = height[i]
#                     i += 1
#             else:
#                 prev = height[j]
#                 j -= 1
#                 while i < j and height[i] >= height[j]:
#                     if prev - height[j] > 0:
#                         volumn += prev - height[j]
#                     else:
#                         prev = height[j]
#                     j -= 1
#         return volumn
