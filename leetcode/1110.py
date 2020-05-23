# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# if a node is to be deleted:
#   1. set it's parent's ref to it as None
#   2. add it's children to the forest if they are not None
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        forest = []
        to_delete = set(to_delete)
        def dfs(root, parent=None):
            if not root:
                return False
            if dfs(root.left):
                root.left = None
            if dfs(root.right):
                root.right = None
            if root.val in to_delete:
                if root.left: forest.append(root.left)
                if root.right: forest.append(root.right)
                return True
            return False

        if not dfs(root):
            forest.append(root)
        return forest
