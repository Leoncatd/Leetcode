# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s :
            return False
        if self.isSametree(s,t):
            return True
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    def isSametree(self, p: TreeNode, q: TreeNode)-> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSametree(p.left,q.left) and self.isSametree(p.right, q.right)
