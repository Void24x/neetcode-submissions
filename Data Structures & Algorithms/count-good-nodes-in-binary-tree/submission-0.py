# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverseAndCount(self, node, prevNodeVal, count):
        if(node is None): return

        if(node.val >= prevNodeVal):
            count[0] += 1
            self.traverseAndCount(node.left, node.val, count)
            self.traverseAndCount(node.right, node.val, count)
        else:
            self.traverseAndCount(node.left, prevNodeVal, count)
            self.traverseAndCount(node.right, prevNodeVal, count)
        return
    def goodNodes(self, root: TreeNode) -> int:
        count = [1]
        self.traverseAndCount(root.left, root.val, count)
        self.traverseAndCount(root.right, root.val, count)
        return count[0]