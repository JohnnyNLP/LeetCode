# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        
        def sibling_check(node):
            if node.left and node.right:
                # x and y are siblings
                if set([node.left.val, node.right.val]) == set([x,y]):
                    return True
            return False
        
        q = collections.deque()
        q.append(root)
        
        while q:
            qLen = len(q) # make sure to traverse one level at a time
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node and not sibling_check(node):
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)              
            print(level)
            if level and (x in level and y in level):
                return True
        
        return False