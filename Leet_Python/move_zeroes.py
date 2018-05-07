
# coding: utf-8

# In[ ]:


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        


# In[35]:


nums = [1,2,3,0,0,3,0,2,3]
nums1 =[]
buf = 0
for i in nums:
    if i == 0:
        buf +=1
    else: nums1.append(i)
for i in range(buf):
    nums1.append(0)
print(nums1)


# In[51]:


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums1 =[]
        buf = 0
        for i in nums:
            if i == 0:
                buf +=1
            else: nums1.append(i)
        for i in range(buf):
            nums1.append(0)
        nums = nums1
test = Solution()
l1 = [1,2,3,0,0,3,0,2,3]
test.moveZeroes(l1)
print(nums1)


# In[50]:


class Solution:
    def moveZeroes(self, nums):
        pos = 0
        for i in xrange(len(nums)):
            if nums[i]:
                nums[pos] = nums[i]
                pos += 1

        for i in xrange(pos, len(nums)):
            nums[i] = 0


# In[52]:


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        moveIndex = 0
        for i in range(0,len(nums)):
            if nums[i]:
                temp = nums[moveIndex]
                nums[moveIndex] = nums[i]
                nums[i] = temp
                moveIndex +=1

