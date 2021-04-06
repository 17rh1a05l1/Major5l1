#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# # Errors and Exceptions Homework

# ### Problem 1
# Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks.

# In[ ]:


for i in ['a','b','c']:
    try:
        print(i**2)
    except:
        print("Not an integer")


# ### Problem 2
# Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks. Then use a <code>finally</code> block to print 'All Done.'

# In[ ]:


x = 5
y = 0
try:
    z = x/y
except:
    print("Zero divided by error")
finally:
    print("All done")


# ### Problem 3
# Write a function that asks for an integer and prints the square of it. Use a <code>while</code> loop with a <code>try</code>, <code>except</code>, <code>else</code> block to account for incorrect inputs.

# In[ ]:


def ask():
     while True:
        try:
            n=int(input("Input an integer:"))
        except:
            print("An error occurred! Please try again!")
        else:
            print("Thank you, your number squared is:",n**2)


# In[ ]:


ask()


# # Great Job!

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




