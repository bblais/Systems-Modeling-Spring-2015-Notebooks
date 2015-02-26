# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ## SIR Model Implementation

# <codecell>

from pyndamics import *

# <codecell>

sim=Simulation()
sim.add("S'=-a*S*I", 100, plot=True)
sim.add("I'=+a*S*I-b*I", 1, plot=True)
sim.add("R'=+b*I", 0, plot=True)
sim.params(a=1,b=1)
sim.run(0,10)

# <markdowncell>

# ## Scenario 2 - All end up in Recovered

# <codecell>

sim=Simulation()
sim.add("S'=-a*S*I", 100, plot=1)
sim.add("I'=+a*S*I-b*I", 1, plot=1)
sim.add("R'=+b*I", 0, plot=1)
sim.params(a=.1,b=1)
sim.run(0,10)

# <markdowncell>

# ## Scenario 3 kind of  - Most end up in I
# 
# (but what if I run longer?)

# <codecell>

sim=Simulation()
sim.add("S'=-a*S*I", 100, plot=1)
sim.add("I'=+a*S*I-b*I", 1, plot=1)
sim.add("R'=+b*I", 0, plot=1)
sim.params(a=1,b=.01)
sim.run(0,10)

# <codecell>

sim=Simulation()
sim.add("S'=-a*S*I", 100, plot=1)
sim.add("I'=+a*S*I-b*I", 1, plot=1)
sim.add("R'=+b*I", 0, plot=1)
sim.params(a=1,b=0)
sim.run(0,10)

# <markdowncell>

# ## Scenario 1 and 4  -  Some (most) still left in S

# <codecell>

sim=Simulation()
sim.add("S'=-a*S*I", 100, plot=1)
sim.add("I'=+a*S*I-b*I", 1, plot=1)
sim.add("R'=+b*I", 0, plot=1)
sim.params(a=.01,b=1)
sim.run(0,100)

# <markdowncell>

# ## SIRS Model

# <codecell>

sim=Simulation()
sim.add("S'=-a*S*I+c*R", 100, plot=1)
sim.add("I'=+a*S*I-b*I", 1, plot=1)
sim.add("R'=+b*I-c*R", 0, plot=1)
sim.params(a=.1,b=1,c=1)
sim.run(0,10)

# <codecell>

sim.S[-1],sim.I[-1],sim.R[-1]

# <markdowncell>

# http://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology

# <codecell>

sim=Simulation()
sim.add("S'=-a*S*I+c*R", 100, plot=1)
sim.add("I'=+a*S*I-b*I", 1, plot=1)
sim.add("R'=+b*I-c*R", 0, plot=1)
sim.params(a=1,b=101,c=1)
sim.run(0,10)

# <codecell>


