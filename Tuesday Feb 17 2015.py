# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from science import *

# <codecell>

pwd

# <codecell>

data=pandas.read_excel('data/s009.xls',skiprows=[0,1])

# <codecell>

data

# <codecell>

t_data=data['day']
y_data=data['height (cm)']
plot(t_data,y_data,'o')

# <markdowncell>

# ## Linear growth example
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
plot(t_data,y_data,'o')

# <markdowncell>

# ## Exponential Growth
# 
# $y'=my$  where $m$ is a growth constant

# <codecell>

y=2
t=0

constant=.06
dt=0.01

# <codecell>

reset()

store(t,y)
for i in range(9000):
    dy=constant*y*dt
    
    y=y+dy
    t=t+dt
    
    if i%100 == 0 :  # if the remainder with i/100 = 0 (i.e. i is divisible by 100)
        store(t,y)

# <codecell>

t,y=recall()

# <codecell>

plot(t,y)
plot(t_data,y_data,'o')

# <codecell>


