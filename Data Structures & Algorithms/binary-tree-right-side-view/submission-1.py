# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverseAndStore(self, root, level, ans):
        if(root is None): return None

        ## For storing only right side element of the tree:
        ##  make sure your are appending element to the list only once for each level
        ##      so only append when level number is equal to as list size 
        if(level == len(ans)):
            ans.append(root.val)
        self.traverseAndStore(root.right, level+1,ans)
        self.traverseAndStore(root.left, level+1,ans)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        ##Do inverse-preorder traversal
        self.traverseAndStore(root, 0, ans)

        return ans

