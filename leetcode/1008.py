# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def bstFromPreorder(l, r):
            """[l, r)"""
            if l >= r: return None
            root = TreeNode(preorder[l])
            if l == r - 1: return root
            anchor = bisect.bisect_left(preorder, preorder[l], l+1, r)
            root.left = bstFromPreorder(l+1, anchor)
            root.right = bstFromPreorder(anchor, r)
            return root
        return bstFromPreorder(0, len(preorder))
