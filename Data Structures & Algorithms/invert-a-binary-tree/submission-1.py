# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case to see if current node is empty for recursion
        if not root:
            return None
        # do the swapping
        root.left, root.right = root.right, root.left
        # then use recursive calls for both left and right nodes
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root