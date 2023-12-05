
# coding: utf-8

# In[ ]:


def func(a):
    print(a)
    a += 1

a = 5
func(a)
print(a)


# In[ ]:


def func(a):
    print(a)
    a += 1
    return a

a = 5
print(func(a))


# In[ ]:


def func(a, b):
    print(a, b)
    a += 1
    b -= 1
    return a, b

a = 5
b = 5
a, b = func(a, b)
print(a, b)


# In[ ]:


def divide(delimoe, delitel): 
    return delimoe // delitel 
print(divide(50,5))
print(divide(delitel=5, delimoe=50)) 


# In[ ]:


def example(a):
    if a>0:
        return "positive"
    else:
        a =- a
print(example(5))
print(example(-5))


# In[ ]:


def rec(a, b):
    if b > 1:
        return a * rec(a, b - 1)
    else:
        return a

print(rec(2, 10))
print(rec(2, 2965))

