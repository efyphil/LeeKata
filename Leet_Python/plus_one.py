
# coding: utf-8

# In[ ]:


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = ''
        for i in digits:
            a += str(i)
        a = int(a) + 1
        digits = []
        for i in str(a):
            digits.append(int(i))
        return  digits


# In[ ]:


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return []
        
        i = len(digits) - 1
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                i -= 1
        if digits[0] == 0:
            return [1]+digits


# In[ ]:


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = 1
        i = len(digits)-1
        while i >=0:
            if digits[i]+flag <10:
                digits[i] = digits[i]+flag
                flag = 0
            else:
                digits[i] = (digits[i]+flag)%10
            i-=1
        if flag == 1:
            digits.insert(0,1)
        return digits


# In[ ]:


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        d = [str(x) for x in digits]
        num = int(''.join(d)) + 1
        
        return list(map(int, str(num)))

