# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total=0
        def dfs(node):
            nonlocal total
            if not node:
                return 
            if low<=node.val and node.val<=high:
                total+=node.val
            if low<node.val:
                dfs(node.left)
            if high>node.val:
                dfs(node.right)
        dfs(root)
        return total
                
        