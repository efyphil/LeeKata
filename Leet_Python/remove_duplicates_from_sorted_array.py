
# coding: utf-8

# In[30]:
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        
        if len(nums)<2:
            return len(nums)
        
        pre = 0
        list1 = [nums[pre]]
        for cur in range(1,len(nums)):
            if nums[cur]!=nums[pre]:
                pre+=1
                nums[pre]=nums[cur]
                list1.append(nums[pre])
        return list1

# In[44]:


# Also work with unsorted list
class SecondSolution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        
        if len(nums)<2:
            return len(nums)
        nums1 = set(nums)
        nums1 = list(nums1)
        return nums1
test1 = Solution()
test2 = SecondSolution()
l1 = [1,2,2,3,3,3,4,5,6]
l2 = [1,4,5,6,3,4,1]
print(test1.removeDuplicates(l1))
print(test1.removeDuplicates(l2))
print(test2.removeDuplicates(l1))
print(test2.removeDuplicates(l2))

