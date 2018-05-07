
# coding: utf-8

# In[1]:


list1 = [1]
def dbl_linear(n):
    u = 1
    u1 = 1 
    y = 0
    z = 0
    m = n
    while n:
        y = 2 * u + 1
        list1.append(y)
        z = 3 * u + 1
        list1.append(z)
        u = y
        n -= 1
    return(list1)
print(dbl_linear(3))

