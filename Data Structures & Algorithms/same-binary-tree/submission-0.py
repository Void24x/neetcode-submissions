# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(p is None and q is None):
            return True
        if ((p is None and q is not None) or (p is not None and q is None)):
            return False
        l,r = True,True
        if(p.val == q.val):
            l = self.isSameTree(p.left, q.left)
            r = self.isSameTree(p.right, q.right)
        else:
            return False
        return l and r