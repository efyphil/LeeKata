
# coding: utf-8

# In[2]:


def DNA_strand(dna):
    newDna = ''
    for i in dna:
        if i == 'A':
            newDna += 'T'
        elif i == 'T':
            newDna += 'A'
        elif i == 'G':
            newDna += 'C'
        elif i == 'C':
            newDna += 'G'
    return newDna
print(DNA_strand("CAAA"))


# In[3]:


def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))


# In[ ]:


pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])

