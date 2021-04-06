#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by CareerEdge</em></center>

# # Object Oriented Programming
# ## Homework Assignment
# 
# #### Problem 1
# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

# In[2]:


class Line:
        def __init__(self,coor1,coor2):
            self.coor1 = coor1
            self.coor2 = coor2
            def distance(self):
                return ((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)**0.5
            def slope(self):
                return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])


# In[2]:


# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)


# In[3]:


li.distance()


# In[4]:


li.slope()


# ________
# #### Problem 2

# Fill in the class 

# In[7]:


class Cylinder:
     pi=3.14
def __init__(self,height=1,radius=1):
    self.height=height
    self.radius=radius
def volume(self):
    return Cylinder.pi*(self.radius**2)*self.height
def surface_area(self):
            c=2*Cylinder.pi*(self.radius**2)
            w=2*Cylinder.pi*self.radius*self.height
            return c+w


# In[6]:


# EXAMPLE OUTPUT
c = Cylinder(2,3)


# In[7]:


c.volume()


# In[8]:


c.surface_area()

