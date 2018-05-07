
# coding: utf-8

# In[ ]:


def filter_list(l):
    return [x for x in l if type(x)==int]


# In[ ]:


def filter_list(l):
    return [i for i in l if not isinstance(i, str)]

