#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://coignite.io'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by CareerEdge</em></center>

# # Object Oriented Programming Challenge
# 
# For this challenge, create a bank account class that has two attributes:
# 
# * owner
# * balance
# 
# and two methods:
# 
# * deposit
# * withdraw
# 
# As an added requirement, withdrawals may not exceed the available balance.
# 
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

# In[10]:


class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance += amount
        print("Deposit Accepted")
    def withdraw(self,amount):
        if self.balance>=amount:
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable")


# In[11]:


# 1. Instantiate the class
acct1 = Account('Jose',100)


# In[12]:


# 2. Print the object
print(acct1)


# In[13]:


# 3. Show the account owner attribute
acct1.owner


# In[14]:


# 4. Show the account balance attribute
acct1.balance


# In[15]:


# 5. Make a series of deposits and withdrawals
acct1.deposit(50)


# In[16]:


acct1.withdraw(75)


# In[17]:


# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)


# ## Good job!
