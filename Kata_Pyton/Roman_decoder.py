
# coding: utf-8

# In[11]:


_rdecode = dict(zip('MDCLXVI', (1000, 500, 100, 50, 10, 5, 1)))
def solution(roman):
    """complete the solution by transforming the roman numeral into an integer"""
    result = 0
    for r, r1 in zip(roman, roman[1:]):
        rd, rd1 = _rdecode[r], _rdecode[r1]
        result += -rd if rd < rd1 else rd
    return result + _rdecode[roman[-1]]
print(solution('XXI'))


# In[ ]:


def solution(roman):
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = max_n = 0
    for c in reversed(roman):
        n = symbols[c]
        result += n if n >= max_n else -n
        max_n = max(max_n, n)
    return result

