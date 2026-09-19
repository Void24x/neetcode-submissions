# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root: Optional[TreeNode], dia:int) -> int:
        if (root == None):
            return 0
        lh = self.height(root.left, dia)
        rh = self.height(root.right, dia)

        dia[0] = max(dia[0], lh+rh)

        return 1 + max(lh,rh)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        self.height(root, diameter)
        return diameter[0]
        

# We'll calcualte the sum of left height and right height at every node.
# Because those left and right height sum will give us the maximum path that canbe obatin THROUGH that node.
# after calculating height we will store that value afte comparing current max value and the sum we obtatin from left and right heigh