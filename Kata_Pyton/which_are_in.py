
# coding: utf-8

# In[6]:


def in_array(array1, array2):
    a_list = []
    result = []
    
    for a1 in array1:
        for a2 in array2:
            if a1 in a2:
                a_list.append(a1)
                
    for i in a_list:
        if i not in result:
            result.append(i)
        
    
    return sorted(result)
print(in_array(['garp', 'arp', 'strong','a'] ,['arpedjo' , 'garpist' , 'garmist', 'stronger', 'stronganger', 'srtrongereger'] ))


# In[3]:


def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})

