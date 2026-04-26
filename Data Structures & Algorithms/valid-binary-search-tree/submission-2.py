# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValid(self,root,rootleft,rootright):
        if root==None:
            return True
        if rootleft and root.val<=rootleft.val:
            return False
        if rootright and root.val>=rootright.val:
            return False
        return self.isValid(root.left,rootleft,root) and self.isValid(root.right,root,rootright)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root,None,None)
        