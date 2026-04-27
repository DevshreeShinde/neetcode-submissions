# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self,root):
        if root==None:
            return
        left=self.traverse(root.left)
        if left:
            return left
        self.count+=1
        if self.count==self.k:
            return root.val
        return self.traverse(root.right)
        
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.count = 0
        return self.traverse(root)
        
        