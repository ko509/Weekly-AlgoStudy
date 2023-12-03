# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/?envType=study-plan-v2&envId=top-interview-150


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        answer = 0
        if root == None:
            return answer
        left_subtree = self.maxDepth(root.left) + 1
        right_subtree = self.maxDepth(root.right) + 1
        answer = max(left_subtree, right_subtree)
        return answer