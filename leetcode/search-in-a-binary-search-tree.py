# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def custom(node):
            if not node:
                return 
            print(node.val)
            if node.val==val:
                return node
            left=custom(node.left)
            if left:
                return left
            
            return custom(node.right)
        return custom(root)

        