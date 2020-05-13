#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt

F = 10
T = 2/F
Fs = 200
Ts = 1/Fs
N = int(T/Ts)

t = np.linspace(0, T, N)
signal = np.sin(2*np.pi*F*t)

plt.plot(t, signal)
plt.show()


# In[11]:


import plotly.express as px
sig = np.array(signal)
time= np.array(t)
fig = px.line(x=time, y=sig, title='sin graph')
fig.show()


# In[38]:


import plotly.graph_objs as go
a=[0.025,0.128]
X=np.array(a)
b=[0.999,0.999]
Y=np.array(b)

fig = go.Figure()         
go.add_Scatter(x = X, y = Y)
fig.show()


# In[19]:


y = sig*0


# In[20]:


y


# In[23]:


z=y.resize(198,refcheck=False)


# In[25]:


c=np.array()


# In[30]:


a = np.array(y)
a_l = a.tolist()
a_l.insert(1,0.128)
a = np.array(a_l)


# In[ ]:





# In[27]:


a = np.array(y)
a_l = a.tolist()
a_l.insert(1,0.025)
a = np.array(a_l)


# In[28]:


a


# In[ ]:




