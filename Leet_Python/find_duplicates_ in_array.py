
# coding: utf-8

# In[18]:


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in nums:
            a = nums.count(i)
            if a>1 : return True
        return False
test1 = Solution()
l2 = [1,1,1,1,1,1,1,1]
print(test1.containsDuplicate(l2))


# In[17]:


class Solution:
    def containsDuplicate(self, nums):
        k=0
        arr = []
        arr[:]= list(set(nums))
        
        if len(arr)<len(nums):
            return True
        else:
            return False
test1 = Solution()
l2 = [1,11]
print(test1.containsDuplicate(l2))

