
# coding: utf-8

# In[ ]:


iparens = iter('(){}[]<>')
parens = dict(zip(iparens, iparens))
closing = parens.values()

def valid_parentheses(astr):
    stack = []
    for c in astr:
        d = parens.get(c, None)
        if d:
            stack.append(d)
        elif c in closing:
            if not stack or c != stack.pop():
                return False
    return not stack


# In[ ]:


def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False


# In[ ]:


import re


_regex = "[^\(|\)]"


def valid_parentheses(string):
    string = re.sub(_regex, '', string)
    while len(string.split('()')) > 1:
        string = ''.join(string.split('()'))
    return string == ''


# In[ ]:


def valid_parentheses(string):
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')' and not stack:
            return False
        elif i == ')':
            stack.pop()
    return not stack

