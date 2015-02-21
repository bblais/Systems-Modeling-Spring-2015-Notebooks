# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ## Question to Hand In - Excel Simulation
# 
# 1. For the following system, write out the discrete simulation equations
# 2. Make an Excel simulation using these equations
# 3. Discuss the result
# 
# \begin{eqnarray}
# x'&=&v\\
# v'&=&k - c\cdot v^2
# \end{eqnarray}
# where $k$ is a constant number, say $k=10$, $c$ is a constant number, say $c=0.1$, and $x$ and $v$ are variables to be simulated.   Use plots of $x(t)$ and $v(t)$ to help.

# <codecell>

from science import *

# <markdowncell>

# Just to compare, here is the 1-variable sim from before...

# <markdowncell>

# ### Linear growth example
# 
# $y' = {\rm constant}$

# <codecell>

y=2
t=0

constant=10
dt=0.01

# <codecell>

reset()

store(t,y)
for i in range(9000):
    dy=constant*dt
    
    y=y+dy
    t=t+dt
    
    if i%100 == 0 :  # if the remainder with i/100 = 0 (i.e. i is divisible by 100)
        store(t,y)

# <codecell>

t,y=recall()

# <codecell>

plot(t,y)
xlabel('time')
ylabel('y')

# <markdowncell>

# ## Answer to the HW question

# <codecell>

x=2
v=1
t=0

k=10
c=0.1
dt=0.0005  # I made the time step smaller, so I can see the beginning

# <codecell>

reset()

store(t,x,v)
for i in range(9000):
    dx=v*dt
    dv=(k-c*v**2)*dt
    
    x=x+dx
    v=v+dv
    t=t+dt
    
    if i%100 == 0 :  # if the remainder with i/100 = 0 (i.e. i is divisible by 100)
        store(t,x,v)

# <codecell>

t,x,v=recall()

# <codecell>

plot(t,x)
xlabel('time')
ylabel('x')

# <codecell>

plot(t,v)
xlabel('time')
ylabel('v')

# <codecell>


