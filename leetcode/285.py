# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.pre = None
        self.successor = None
        def inorderTraverse(root):
            if not root:
                return
            if inorderTraverse(root.left):
                return True
            if self.pre == p.val:
                self.successor = root
                return True
            self.pre = root.val
            if inorderTraverse(root.right):
                return True
        inorderTraverse(root)
        return self.successor
