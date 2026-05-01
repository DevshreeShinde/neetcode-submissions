# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        #remove all nodes with given val
        # if root==None:
        #     return None
        # root.left = self.removeLeafNodes(root.left,target)
        # root.right = self.removeLeafNodes(root.right,target)
        # if root.val==target:
        #     if not root.left and not root.right:
        #         return None
        #     if not root.left:
        #         return root.right
        #     elif not root.right:
        #         return root.left
        #     else:
        #         curr = root.left
        #         while curr.right:
        #             curr= curr.right
        #         curr.right=root.right
        #         return root.left
        # return root

        #remove on leaf nodes
        if root==None:
            return None
        root.left = self.removeLeafNodes(root.left,target)
        root.right = self.removeLeafNodes(root.right,target)
        if root.val==target:
            if not root.left and not root.right:
                return None
        return root
        