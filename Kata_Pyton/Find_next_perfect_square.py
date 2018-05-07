
# coding: utf-8

# In[1]:


from math import sqrt
def find_next_square(sq):
    if float(sqrt(sq)) == int(sqrt(sq)):
        return (sqrt(sq) + 1)**2
    else: return -1


# In[14]:


def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1

