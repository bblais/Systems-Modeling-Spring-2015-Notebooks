# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from pyndamics import *

# <markdowncell>

# http://en.wikipedia.org/wiki/Lorenz_system

# <codecell>

sim=Simulation()
sim.add("x'=sigma*(y-x)",14,plot=True)
sim.add("y'=x*(rho-z)-y",8.1,plot=True)
sim.add("z'=x*y-beta*z",45,plot=True)
sim.params(sigma=10,beta=8.0/3,rho=15)
sim.run(0,50)

# <codecell>

phase_plot(sim,'x','y')

# <codecell>

sim.run(0,50,num_iterations=10000)

# <codecell>

phase_plot(sim,'x','y')

# <markdowncell>

# ## Larger $\rho$

# <codecell>

sim=Simulation()
sim.add("x'=sigma*(y-x)",14,plot=True)
sim.add("y'=x*(rho-z)-y",8.1,plot=True)
sim.add("z'=x*y-beta*z",45,plot=True)
sim.params(sigma=10,beta=8.0/3,rho=28)
sim.run(0,50)

# <markdowncell>

# ## What happens in the case of starting with slightly different initial conditions?

# <codecell>

sim=Simulation()
sim.add("x'=sigma*(y-x)",14,plot=1)
sim.add("y'=x*(rho-z)-y",8.1,plot=2)
sim.add("z'=x*y-beta*z",45,plot=3)

sim.add("x2'=sigma*(y2-x2)",16,plot=1)
sim.add("y2'=x2*(rho-z2)-y2",8.1,plot=2)
sim.add("z2'=x2*y2-beta*z2",45,plot=3)

sim.params(sigma=10,beta=8.0/3,rho=15)
sim.run(0,50,num_iterations=10000)

subplot(1,2,1)
phase_plot(sim,'x','y')
phase_plot(sim,'x2','y2')

subplot(1,2,2)
phase_plot(sim,'x','z')
phase_plot(sim,'x2','z2')

# <codecell>


