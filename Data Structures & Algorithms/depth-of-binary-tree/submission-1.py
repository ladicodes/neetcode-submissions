# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, depth=1):
            if not node:
                return 0
            left_depth = dfs(node.left, depth + 1)
            right_depth = dfs(node.right, depth + 1)
            longest_path = max(depth, left_depth, right_depth)
            return longest_path

        return dfs(root)
            
            

        