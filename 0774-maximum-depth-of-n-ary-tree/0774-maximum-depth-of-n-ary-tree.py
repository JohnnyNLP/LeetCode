"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        
        # #DFS
        # stack = []
        # if root:
        #     # root and level
        #     stack.append((root, 1))
        # depth = 0
        # while stack :
        #     (node, level) = stack.pop()
        #     depth = max(depth, level)
        #     for child in node.children:
        #         stack.append((child, level+1))
        # return depth

        # BFS
        queue = []
        if root: queue.append((root, 1))
        depth = 0
        for (node, level) in queue:
            depth = level
            for child in node.children:
                queue.append((child, level+1))
        return depth
        