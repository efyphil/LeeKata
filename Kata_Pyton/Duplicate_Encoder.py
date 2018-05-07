
# coding: utf-8

# In[3]:


def duplicate_encode(word):
    word = word.lower()
    newword = ''
    for i in word:
        if word.count(i) > 1:
            newword += ')'
        else : newword += '('
    return newword
print(duplicate_encode("recede"))


# In[ ]:


def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

