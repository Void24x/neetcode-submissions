# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverseAndStore(self, root, nodeList):
        if not root: return

        self.traverseAndStore(root.left, nodeList)

        nodeList.append(root.val)

        self.traverseAndStore(root.right, nodeList)

        return


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodeList = []

        self.traverseAndStore(root, nodeList)

        return nodeList[k-1]
        
