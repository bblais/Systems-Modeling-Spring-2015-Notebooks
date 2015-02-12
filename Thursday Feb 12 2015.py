# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

%gui tk
from turtle import *

# <codecell>

reset()

#speed("fastest")
current_color="red"
other_color="black"

for i in range(160):
    pencolor(current_color)
    forward(150)
    backward(150)
    left(3)

    # comment - swap the colors
    if i%3==0:
        current_color,other_color=other_color,current_color

# <codecell>

current_color,other_color=other_color,current_color
print "Current: ",current_color
print "Other: ",other_color

# <markdowncell>

# ## Simulation example

# <codecell>

from science import *

# <codecell>

x=2
t=0

constant=10
dt=0.01

# <codecell>

reset()

store(t,x)
for i in range(1000):
    dx=constant*dt
    
    x=x+dx
    t=t+dt
    
    store(t,x)

# <codecell>

t,x=recall()

# <codecell>

x

# <codecell>

plot(t,x)

# <markdowncell>

# ### second simulation

# <codecell>

x=2
t=0

constant=3
dt=0.01

# <codecell>

reset()

store(t,x)
for i in range(1000):
    dx=constant*x*dt
    
    x=x+dx
    t=t+dt
    
    store(t,x)

# <codecell>

t,x=recall()

# <codecell>

plot(t,x)

# <codecell>


