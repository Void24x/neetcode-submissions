# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root: Optional[TreeNode], ans:bool) ->int:
        if not root:
            return 0
        lh = self.height(root.left, ans)
        rh = self.height(root.right, ans)

        # if(abs(lh-rh)<=1):
        #     return 1 + max(lh,rh)

        if(abs(lh-rh) <=1 ):
            ans[0]  = ans[0] and True
        else:
            ans[0]  = ans[0] and False

        return 1 + max(lh,rh)
         
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = [True]
        self.height(root,ans)
        return ans[0]
        