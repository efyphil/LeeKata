
# coding: utf-8

# In[34]:


def tribonacci(s,n):
    for c in range(n - 3):
        s += [s[c] + s[c+1] + s[c+2]]
    return s[0:n]
print(tribonacci([1,1,1],-1))


# In[36]:


def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3):
        res.append(sum(res[-3:]))
    return res

