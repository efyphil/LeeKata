
# coding: utf-8

# In[29]:


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix) - i - 1):
                matrix[i][j], matrix[n - j - 1][n - i - 1] = matrix[n - j - 1][n - i - 1], matrix[i][j]
        matrix.reverse()


# In[35]:


class Solution2:
    def rotate(self, matrix):
        return [list(reversed(x)) for x in zip(*matrix)]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution2().rotate(matrix))


# In[30]:




