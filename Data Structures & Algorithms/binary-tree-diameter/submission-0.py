# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeheight(self,root)->int:
        if root==None:
            return 0
        return 1+max(self.treeheight(root.left),self.treeheight(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        lheight = self.treeheight(root.left)
        rheight = self.treeheight(root.right)
        currdia = lheight+rheight

        ldia = self.diameterOfBinaryTree(root.left)
        rdia = self.diameterOfBinaryTree(root.right)

        return max(currdia,ldia,rdia)
