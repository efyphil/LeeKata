
# coding: utf-8

# In[ ]:


def find_it(seq):
    for num in seq:
        if seq.count(num)%2==1:
            return num
    return None


# In[ ]:


def find_it(seq):
    nums = set()
    for num in seq:
        if num in nums:
            nums.remove(num)
        else:
            nums.add(num)
    return nums.pop()

