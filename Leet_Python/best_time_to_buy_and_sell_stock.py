
# coding: utf-8

# In[16]:


class Solution: 
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """   
        profit = 0
        for i in range(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i])
        return profit
test = Solution()
l1 =[1,2,1,3,4]
print(test.maxProfit(l1))

