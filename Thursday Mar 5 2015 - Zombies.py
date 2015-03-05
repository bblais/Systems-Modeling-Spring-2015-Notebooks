# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from pyndamics import *

# <codecell>

sim=Simulation()
sim.add("S'=b-a*S*Z-e*S",500,plot=1)
sim.add("Z'=a*S*Z+d*R-c*S*Z",1,plot=1)
sim.add("R'=+e*S+c*S*Z-d*R",0,plot=1)
sim.params(a=.0095,b=0,c=.005,d=0,e=.0001)
sim.run(0,5)

# <codecell>

sim=Simulation()
sim.add("S'=b-a*S*Z-e*S",500,plot=1)
sim.add("Z'=a*S*Z+d*R-c*S*Z",1,plot=1)
sim.add("R'=+e*S+c*S*Z-d*R",0,plot=1)
sim.params(a=.0095,b=0,c=.005,d=.0001,e=.0001)
sim.run(0,50000)

# <markdowncell>

# ## Can the S win?

# <codecell>

sim=Simulation()
sim.add("S'=b-a*S*Z-e*S",500,plot=1)
sim.add("Z'=a*S*Z+d*R-c*S*Z",20,plot=1)
sim.add("R'=+e*S+c*S*Z-d*R",0,plot=1)
sim.params(a=.0095,b=0,c=.01,d=0,e=.0001)
sim.run(0,50)

# <codecell>


