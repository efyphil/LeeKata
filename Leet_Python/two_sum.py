
# coding: utf-8

# In[62]:


class Solution:
    def twoSum(self, nums, target):        
        for i in range (len(nums) - 1):
            for j in range (i + 1, len(nums)):
                if target == nums[i]+nums[j]:
                    return [i,j]
nums = [3,2,4]
target = 5
test = Solution()
print(test.twoSum(nums, target))


# In[59]:


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        k = 0
        for i in nums:
            j = target - i
            k += 1
            tmp_nums = nums[k:]
            if j in tmp_nums:
                return [k - 1, tmp_nums.index(j) + k]
nums = [3,2,4]
target = 6
test = Solution()
print(test.twoSum(nums, target))


# In[ ]:


class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            rem = target - num
            if rem in num_dict:
                return [num_dict[rem], i]
            num_dict[num] = i
        return None

