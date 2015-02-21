# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from pyndamics import *

# <codecell>

sim=Simulation()
sim.add("y'=constant",5,plot=True)
sim.params(constant=.1)
sim.run(0,10)

# <markdowncell>

# ## Another example - exponential!

# <codecell>

sim=Simulation()
sim.add("y'=a*y",0.1,plot=True)
sim.params(a=.02)
sim.run(0,90)

# <markdowncell>

# what happens if I run longer?

# <codecell>

sim=Simulation()
sim.add("y'=a*y",0.1,plot=True)
sim.params(a=.02)
sim.run(0,900)

# <markdowncell>

# ## yet another example - logistic!
# 
# * $y'=ay\cdot (K-y)$
# * $K=100$
# * $a=0.02$
# * $t$ from 0 to 90
# * initia value of $y=0.1$

# <codecell>

sim=Simulation()
sim.add("y'=a*y*(1-y/K)",0.1,plot=True)
sim.params(a=.02,K=100)
sim.run(0,90)

# <markdowncell>

# what happens when I run longer?

# <codecell>

sim=Simulation()
sim.add("y'=a*y*(1-y/K)",0.1,plot=True)
sim.params(a=.02,K=100)
sim.run(0,900)

# <markdowncell>

# ## Example from HW

# <codecell>

sim=Simulation()
sim.add("x'=v",0,plot=True)
sim.add("v'=k-c*v**2",0,plot=True)
sim.params(k=5,c=.1)
sim.run(0,10)

# <codecell>

sim=Simulation()
sim.add("x'=v",0,plot=True)
sim.add("v'=k-c*v**2",0,plot=True)
sim.params(k=10,c=.1)
sim.run(0,2)

# <codecell>


