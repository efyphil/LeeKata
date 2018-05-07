
# coding: utf-8

# In[54]:


def Descending_Order1(num):
    a = sorted(list(str(num)),reverse = True)
    a = [int(i) for i in a]
    sum = 0
    for i in a: 
        sum = sum * 10 + i
    return sum
Descending_Order(4567459)


# In[55]:


def Descending_Order2(num):
    return int("".join(sorted(str(num), reverse=True)))
Descending_Order(4567459)


# In[57]:


def Descending_Order3(num):
    #Bust a move right here
    numArr = map(int, str(num))
    print (sorted(numArr,reverse=True))
    desNum = ''
    for i in sorted(numArr,reverse=True):
        desNum = desNum + str(i)
    return int(desNum)
Descending_Order(4567459)

