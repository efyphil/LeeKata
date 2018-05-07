
# coding: utf-8

# In[22]:


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        """
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
l1 = [1,2]
test.rotate(l1,0)
print(l1)

