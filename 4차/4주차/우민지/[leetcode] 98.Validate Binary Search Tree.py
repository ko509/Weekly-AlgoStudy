# https://leetcode.com/problems/binary-search-tree-iterator/?envType=study-plan-v2&envId=top-interview-150
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBST(root: Optional[TreeNode], minNode: Optional[TreeNode], maxNode: Optional[TreeNode]) -> bool:

            if root == None:  # BST 탐색 재귀 함수 탈출 조건
                return True
            if minNode and root.val <= minNode.val: # BST 의 조건에 맞지 않는 경우 (1)
                return False
            if maxNode and root.val >= maxNode.val: # # BST 의 조건에 맞지 않는 경우 (2)
                return False
            return isValidBST(root.left, minNode, root) and isValidBST(root.right, root, maxNode) # left subtree && right subtree 모두 검증하기

        return isValidBST(root, None, None)

