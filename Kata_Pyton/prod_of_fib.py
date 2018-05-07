
# coding: utf-8

# In[ ]:


class Fib(object):

    """docstring for Fib"""

    def __init__(self):
        super(Fib, self).__init__()
        self._a = 0
        self._b = 1

    def __call__(self):
        self._a, self._b = self._b, self._a + self._b
        return self._a, self._b

def productFib(prod):
    # your code
    fib = Fib()
    a, b = fib()
    while (a * b) < prod:
        a, b = fib()

    return [a, b, (a * b) == prod]


# In[ ]:


def productFib(prod):
    a,b = 0,1
    while a*b < prod:
        a,b = b, b+a
    return [a, b, a*b == prod]

