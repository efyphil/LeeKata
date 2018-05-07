
# coding: utf-8

# In[19]:


def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
        else: return True
    else: return False
print(is_prime(7))


# In[ ]:


def is_prime(num):
    if num < 2:
        return False
      
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# In[ ]:


def is_prime(num):
    return num > 1 and not any(num % n == 0 for n in range(2,num))

