# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self,node, lb, rb):
        if node is None: return True

        l,r = True, True

        if(node.left):
            if(node.left.val > lb and node.left.val < node.val):
                l = self.check(node.left,lb,node.val)
            else:
                return False
        if(node.right):
            if(node.right.val < rb and node.right.val > node.val):
                r = self.check(node.right, node.val, rb)
            else:
                return False
        return l and r
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lb= float('-inf')
        rb = float('inf')

        return self.check(root, lb, rb)
        