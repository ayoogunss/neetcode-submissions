# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case to know if tree is same
        if p == None and q == None:
            return True
        #if one of them is null (different size) then diff tree
        if p == None or q == None:
            return False
        # if node have different values then diff tree
        if p.val != q.val:
            return False
        #keep traversing left and right nodes to see if the same
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)