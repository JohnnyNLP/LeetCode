# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(root) :
            # Returns 'balanced' label and 'depth'
            if root is None: return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)
            # left subtree is balanced, right subtree is balanced,
            # and the depth difference is less or equal to 1 => balanced
            balanced = (left[0] and right[0]
                        and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]
            
        return dfs(root)[0]