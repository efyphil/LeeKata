
# coding: utf-8

# In[55]:


def get_sum1(a,b):
    if a < b:
        sum = a
        while a!= b:
            a += 1
            sum += a
    else:
        sum = b
        while b != a:
            b += 1
            sum += b
    return sum
print(get_sum1(-1,2))


# In[44]:


def get_sum2(a,b):
    if a > b:
        a,b = b,a
    sum = a
    while a!= b:
        a += 1
        sum += a
    return sum
print(get_sum2(-1,1))


# In[67]:


def get_sum3(a,b):
    return sum(range(min(a,b),max(a,b)+1)) 
print(get_sum3(-1,2))


# In[57]:


def get_sum4(a,b):
    return sum(range(min(a,b), max(a,b)+1))
print(get_sum4(2,-1))


# In[62]:


def get_sum5(a,b):
    return (a+b)*(abs(a-b)+1)//2
print(get_sum5(-1,2))

