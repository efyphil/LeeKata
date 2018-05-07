
# coding: utf-8

# In[63]:


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
            
        return ans
test = Solution()
l1 = [1,1,1,1,2,1,1]
l2 = [2,1,1]
print(test.intersect(l1,l2))


# In[35]:


class Solution:
    def intersect(self, nums1, nums2):
        memo, res = {}, []
        for n1 in nums1:
            if n1 not in memo:
                memo[n1] = 1
            else:
                memo[n1] += 1
        for n2 in nums2:
            if n2 in memo and memo[n2]:
                res.append(n2)
                memo[n2] -= 1
        return res
test = Solution()
l1 = [1,1,1,1,1,1]
l2 = [2,1,1]
print(test.intersect(l1,l2))


# In[58]:


memo = {}
res =[]
nums1 = [1,3,1,1,2,3]
nums2 = [1,1,2,1,3,3]
for n1 in nums1:
    if n1 not in memo:
        memo[n1] = 1
    else:
        memo[n1] += 1
print(memo)
for n2 in nums2:
    if n2 in memo and memo[n2]:
        res.append(n2)
        memo[n2] -= 1
print(memo)
print(res)

