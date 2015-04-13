# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from pyndamics import *
from pyndamics.emcee import *
import pandas

# <markdowncell>

# ## Data from homework

# <codecell>

with open('zombie_data.csv','w') as fid:
    fid.write("""time    zombies
    0.00    0
    3.00    1
    5.00    2
    6.00    2
    8.00    3
    10.00   3
    22.00   4
    22.20   6
    22.50   2
    24.00   3
    25.50   5
    26.00   12
    26.50   15
    27.50   25
    27.75   37
    28.50   25
    29.00   65
    29.50   80
    31.50   100""")

# <codecell>

data=pandas.read_csv('zombie_data.csv', delim_whitespace=True)
data

# <codecell>

sim=Simulation()
sim.add("S'=-beta*S*Z",300,plot=1)
sim.add("Z'=+beta*S*Z-gamma*Z",0.1,plot=2)
sim.add("R'=gamma*Z",0,plot=1)
sim.add_data(t=data['time'],Z=data['zombies'],plot=2)
sim.params(beta=.001,gamma=.03)
sim.run(0,50)

# <codecell>

model=MCMCModel(sim,beta=Uniform(0,0.001),gamma=Uniform(0,.1))

# <codecell>

model.run_mcmc(500)
model.plot_chains()

# <codecell>

model.set_initial_values('samples')
model.run_mcmc(500)
model.plot_chains()

# <codecell>

model.plot_distributions()

# <codecell>

model.triangle_plot()

# <codecell>

sim.run(0,50)

# <codecell>

sim.beta

# <codecell>

model.median_values

# <codecell>

model=MCMCModel(sim,beta=Uniform(0,0.01),gamma=Uniform(0,.1),initial_Z=Uniform(0,1))
model.run_mcmc(500)
model.plot_chains()

# <codecell>

model.set_initial_values('samples')
model.run_mcmc(500)
model.plot_chains()

# <codecell>

model.plot_distributions()

# <codecell>

model.triangle_plot()

# <codecell>

sim.noplots=True  # turn off the simulation plots
for i in range(500):
    model.draw()
    sim.run(0,50)
    plot(sim.t,sim.Z,'g-',alpha=.05)
sim.noplots=False  # gotta love a double-negative
plot(data['time'],data['zombies'],'bo')  # plot the data

# <codecell>


