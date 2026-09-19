# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverseAndStore(self, root, level, ans):
        if(root is None): return None

        if(level == len(ans)):
            ans.append(root.val)
        self.traverseAndStore(root.right, level+1,ans)
        self.traverseAndStore(root.left, level+1,ans)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        self.traverseAndStore(root, 0, ans)

        return ans