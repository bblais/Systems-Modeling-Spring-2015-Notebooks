# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from pyndamics import *
from pyndamics.emcee import *

# <codecell>

x=linspace(0,20,100)
y=0.1*x+3+randn(len(x))
plot(x,y,'o')

# <codecell>

sim=Simulation()
sim.add("y'=a",1,plot=True)
sim.params(a=0.05)
sim.add_data(t=x,y=y,plot=True)
sim.run(0,20)

# <codecell>

model=MCMCModel(sim,a=Uniform(-1,1))

# <codecell>

model.run_mcmc(500)
model.plot_chains()

# <codecell>

sim.run(0,20)

# <codecell>

model.plot_distributions()

# <markdowncell>

# ## Fitting the initial value

# <codecell>

model=MCMCModel(sim,
            a=Uniform(-1,1),
            initial_y=Uniform(-5,10),  # a nice wide range
            )
model.run_mcmc(500)
model.plot_chains()

# <codecell>

sim.run(0,20)
model.plot_distributions()

# <codecell>


