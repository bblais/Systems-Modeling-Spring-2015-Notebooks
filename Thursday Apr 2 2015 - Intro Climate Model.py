# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from pyndamics import *

# <markdowncell>

# ## No atmosphere

# <codecell>

sim=Simulation()
sim.add("Es'=C*(100-0.3*100-Es)",1,plot=True)
sim.params(C=1)
sim.run(0,50)

# <codecell>

sim=Simulation()
sim.add("Es'=C*(100-albedo*100-Es)",1,plot=True)
sim.add("Ts=88.5*Es**0.25-273",plot=True)
sim.params(C=1,albedo=0.3)
sim.run(0,50)

# <codecell>

sim.Ts[-1]

# <markdowncell>

# ## With an atmosphere, complete absorption of the surface energy

# <codecell>

sim=Simulation()
sim.add("Es'=C1*(100-albedo*100+Ea-Es)",1,plot=1)
sim.add("Ea'=C2*(Es-Ea-Ea)",1,plot=1)
sim.add("Ts=88.5*Es**0.25-273",plot=2)
sim.add("Ta=88.5*Ea**0.25-273",plot=2)
sim.params(C1=1,C2=10,albedo=0.3)
sim.run(0,50)

# <codecell>

sim.Ts[-1]

# <markdowncell>

# ## With partial absorption

# <codecell>

sim=Simulation()
sim.add("Es'=C1*(100-albedo*100+Ea-Es)",1,plot=1)
sim.add("Ea'=C2*(g*Es-Ea-Ea)",1,plot=1)
sim.add("Ts=88.5*Es**0.25-273",plot=2)
sim.add("Ta=88.5*Ea**0.25-273",plot=2)
sim.params(C1=1,C2=10,albedo=0.3,g=0.9)
sim.run(0,50)

# <codecell>

sim.Ts[-1]

# <markdowncell>

# what happens if g=0?

# <codecell>

sim=Simulation()
sim.add("Es'=C1*(100-albedo*100+Ea-Es)",1,plot=1)
sim.add("Ea'=C2*(g*Es-Ea-Ea)",1,plot=1)
sim.add("Ts=88.5*Es**0.25-273",plot=2)
#sim.add("Ta=88.5*Ea**0.25-273",plot=2)
sim.params(C1=1,C2=10,albedo=0.3,g=0.0)
sim.run(0,50)

# <codecell>

sim.Ts[-1]

# <codecell>


