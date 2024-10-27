# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dc(values):
            if not values:
                return
            max_val=max(values)
            max_index=values.index(max_val)
            root=TreeNode(max_val)
            root.left=dc(values[:max_index])
            root.right=dc(values[max_index+1:])
            return root
        return dc(nums)
            
        