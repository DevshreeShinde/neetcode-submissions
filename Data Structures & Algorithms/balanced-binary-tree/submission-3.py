# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def heighttree(self, root):
        if root==None:
            return 0
        return 1+max(self.heighttree(root.left),self.heighttree(root.right))
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        # if root.left==None and root.right==None:
        #     return True
        lheight=self.heighttree(root.left)
        rheight=self.heighttree(root.right)
        if abs(rheight-lheight)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)