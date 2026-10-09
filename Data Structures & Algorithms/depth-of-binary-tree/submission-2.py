# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case for recursion
        if root == None:
            return 0
        # return value of 1 and get the largest depth between left and right trees
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))