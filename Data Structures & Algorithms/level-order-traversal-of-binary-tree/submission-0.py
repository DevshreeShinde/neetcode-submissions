# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        ans = []
        store = [root]
        while store:
            currlevel = []
            for i in range(len(store)):
                curr = store.pop(0)
                if curr:
                    currlevel.append(curr.val)
                if curr and curr.left:
                    store.append(curr.left)
                if curr and curr.right:
                    store.append(curr.right)
            ans.append(currlevel)
        return ans