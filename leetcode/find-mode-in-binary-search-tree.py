# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mylist=[]
        def custom(node):
            if node==None:
                return
            custom(node.left)
            mylist.append(node.val)
            custom(node.right)
        custom(root)
        freq=dict(Counter(mylist))
        max_val=max(freq.values())
        mode=[key for key,values in freq.items() if values==max_val]
       
        return mode

        
        