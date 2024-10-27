# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def custom(node,path):
            if len(path)>=k:
                return path[k-1]
            if not node:
                return 
            
            left=custom(node.left,path)
            if left:
                return left
            path.append(node.val)
            print(path)
            return custom(node.right,path)
        return custom(root,[])

        