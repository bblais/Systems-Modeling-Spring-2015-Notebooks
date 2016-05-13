
# coding: utf-8

# In[1]:

from pyndamics import *


# ## No atmosphere

# In[2]:

sim=Simulation()
sim.add("Es'=C*(100-0.3*100-Es)",1,plot=True)
sim.params(C=1)
sim.run(0,50)


# In[23]:

sim=Simulation()
sim.add("Es'=C*(100-albedo*100-Es)",1,plot=True)
sim.add("Ts=88.5*Es**0.25-273",plot=True)
sim.params(C=1,albedo=0.3)
sim.run(0,50)


# In[24]:

sim.Ts[-1]


# ## With an atmosphere, complete absorption of the surface energy

# In[15]:

sim=Simulation()
sim.add("Es'=C1*(100-albedo*100+Ea-Es)",1,plot=1)
sim.add("Ea'=C2*(Es-Ea-Ea)",1,plot=1)
sim.add("Ts=88.5*Es**0.25-273",plot=2)
sim.add("Ta=88.5*Ea**0.25-273",plot=2)
sim.params(C1=1,C2=10,albedo=0.3)
sim.run(0,50)


# In[16]:

sim.Ts[-1]


# ## With partial absorption

# In[17]:

sim=Simulation()
sim.add("Es'=C1*(100-albedo*100+Ea-Es)",1,plot=1)
sim.add("Ea'=C2*(g*Es-Ea-Ea)",1,plot=1)
sim.add("Ts=88.5*Es**0.25-273",plot=2)
sim.add("Ta=88.5*Ea**0.25-273",plot=2)
sim.params(C1=1,C2=10,albedo=0.3,g=0.9)
sim.run(0,50)


# In[18]:

sim.Ts[-1]


# what happens if g=0?

# In[20]:

sim=Simulation()
sim.add("Es'=C1*(100-albedo*100+Ea-Es)",1,plot=1)
sim.add("Ea'=C2*(g*Es-Ea-Ea)",1,plot=1)
sim.add("Ts=88.5*Es**0.25-273",plot=2)
#sim.add("Ta=88.5*Ea**0.25-273",plot=2)
sim.params(C1=1,C2=10,albedo=0.3,g=0.0)
sim.run(0,50)


# In[22]:

sim.Ts[-1]


# In[ ]:



