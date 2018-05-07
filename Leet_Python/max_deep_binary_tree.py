
# coding: utf-8

# In[11]:


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
root = TreeNode(44)
root.left = TreeNode(111)
root.right = TreeNode(111)
root.left.left = TreeNode(10)
root.left.left.left = TreeNode(24)
print (Solution().maxDepth(root))


# In[ ]:


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bfs(self, root):
        queue = [root] if root else []
        max_depth = 0
        while queue:
            max_depth += 1
            next_q = []
            for node in queue:
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            queue = next_q
        return max_depth
        
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.bfs(root)

