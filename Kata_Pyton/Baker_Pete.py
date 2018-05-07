
# coding: utf-8

# In[20]:


def cakes(recipe, available):
    list = []
    for ingredient in recipe:
        if ingredient in available:
            list.append(available[ingredient]/recipe[ingredient])
        else:
            return 0
    return min(list)
recipe = {"flour": 500, "sugar": 200, "eggs": 1, }
available = {"flour": 1200, "sugar": 1200, "eggs": 5}
print(cakes(recipe,available))


# In[21]:


def cakes(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)

