
# coding: utf-8

# In[8]:


def likes(names):
    if names == []:
        print('no one likes this')
    elif len(names) == 1:
        print( names[0] , 'likes this')
    elif len(names) == 2:
        print( names [0] , 'and' , names[1] , 'like this')
    elif len(names) == 3:
        print( names[0] ,names[1] , 'and' , names [2] , 'like this')
    else :
        print( names[0] , names[1], 'and 2 others like this')
likes([])


# In[ ]:


def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

