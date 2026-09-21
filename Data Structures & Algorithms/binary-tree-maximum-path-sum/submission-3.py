# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solution(self, root, ans):
        if not root: return 0

        leftsum = max(0,self.solution(root.left,ans))
        rightsum = max(0,self.solution(root.right,ans))

        ans[0] = max(ans[0], leftsum + rightsum + root.val)

        return root.val + max(leftsum, rightsum)


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [float('-inf')]

        self.solution(root,ans)

        return ans[0]
        